from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Input acquisition - receive both parameters as string (may be empty)
        params = agent.receive_parameters(['query', 'date'])  # Expect string values
        query = params.get('query', '').strip()
        date = params.get('date', '').strip()

        # Determine operational mode
        base_url = "https://api.coingecko.com/api/v3"
        result = None

        if query:  # Crypto search mode
            endpoint = f"{base_url}/search"
            response = requests.get(endpoint, params={'query': query}, timeout=15)
            response.raise_for_status()
            result_data = response.json()
            # Serialization check - ensure output is JSON-serializable dict
            agent.send_output(
                agent_output_name='search_results',
                agent_result=result_data
            )
            return

        elif date:  # Price history mode, default to bitcoin, date expected in 'DD-MM-YYYY'
            coin_id = "bitcoin"
            endpoint = f"{base_url}/coins/{coin_id}/history"
            response = requests.get(endpoint, params={'date': date}, timeout=15)
            response.raise_for_status()
            result_data = response.json()
            # Serialization check - ensure output is JSON-serializable dict
            agent.send_output(
                agent_output_name='history_result',
                agent_result=result_data
            )
            return

        # If neither parameter provided, guide invocation
        user_input = agent.receive_parameter('user_input')  # Facilitate pipeline discovery
        agent.send_output(
            agent_output_name='error',
            agent_result='Error: Please provide at least one parameter: "query" (for crypto search) or "date" (for price history), both as strings.'
        )
    except Exception as e:
        # Comprehensive error handling and serialization of error message
        agent.send_output(
            agent_output_name='error',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='CryptoHistoryQueryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
