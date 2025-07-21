from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

"""
Dependencies:
- requests

Ensure you have 'requests' installed in your environment:
pip install requests
"""

@run_agent
def run(agent: MofaAgent):
    # No required input, but to facilitate calls from other nodes:
    user_input = agent.receive_parameter('user_input')
    try:
        # Fetch a random Kimi Räikkönen quote
        response = requests.get('https://kimiquotes.pages.dev/api/quote', timeout=10)
        response.raise_for_status()
        data = response.json()  # Should be serializable (dict)
        agent.send_output(
            agent_output_name='kimi_quote',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='kimi_quote',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='KimiQuotesFetcherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
