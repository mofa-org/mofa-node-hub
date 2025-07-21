from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate input compatibility for chained calls, although the API requires no input
        user_input = agent.receive_parameter('user_input')

        endpoint = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        quotes = response.json()

        # Ensure output is always serializable and valid
        if isinstance(quotes, list):
            result = {'quote': quotes[0] if quotes else ''}
        else:
            result = {'quote': str(quotes)}

        agent.send_output(
            agent_output_name='ron_swanson_quote',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='ron_swanson_quote',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='RonSwansonQuoteNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
