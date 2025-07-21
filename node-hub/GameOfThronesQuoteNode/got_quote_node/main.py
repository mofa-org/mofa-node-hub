from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate dataflow, receive a dummy input
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://api.gameofthronesquotes.xyz/v1/random', timeout=10)
        response.raise_for_status()
        # Ensure the output is serializable (API returns JSON)
        quote_data = response.json()
        agent.send_output(
            agent_output_name='got_quote',
            agent_result=quote_data
        )
    except Exception as e:
        # Error handling within the agent
        agent.send_output(
            agent_output_name='got_quote',
            agent_result={
                'error': True,
                'message': f'Failed to retrieve quote: {str(e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='GameOfThronesQuoteNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
