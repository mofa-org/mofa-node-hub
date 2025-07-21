from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # No input required, facilitate potential input connections
        user_input = agent.receive_parameter('user_input')  # For framework pipeline compatibility
        
        api_url = 'https://api.fisenko.net/v1/quotes/en'
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()

        # The API returns JSON with a random quote
        data = response.json()  # Already serializable (dict)

        # Validate output serialization
        agent.send_output(
            agent_output_name='quote_output',
            agent_result=data  # dict; should be serializable
        )
    except Exception as e:
        # Catch all errors and return as string for error port
        agent.send_output(
            agent_output_name='quote_output',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='QuoteRetrievalNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
