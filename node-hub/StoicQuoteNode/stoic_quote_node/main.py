# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    StoicQuoteNode Agent
    Retrieves a stoicism quote from https://stoic.tekloon.net/stoic-quote
    Input: user_input (required for dora-rs input compatibility)
    Output: {'quote': str, 'author': str}
    """
    # Input compatibility - facilitate calls, though not used
    user_input = agent.receive_parameter('user_input')
    api_url = "https://stoic.tekloon.net/stoic-quote"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure only serializable subset is selected
        serialized_output = {
            'quote': str(data.get('quote', '')),
            'author': str(data.get('author', ''))
        }
        agent.send_output(
            agent_output_name='stoic_quote',
            agent_result=serialized_output
        )
    except Exception as e:
        # Handle and serialize error
        error_output = {
            'error': str(e)
        }
        agent.send_output(
            agent_output_name='stoic_quote',
            agent_result=error_output
        )

def main():
    agent = MofaAgent(agent_name='StoicQuoteNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
