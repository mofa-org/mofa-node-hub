# Dependencies:
#   - requests (install via pip if not present)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent to fetch Magic The Gathering information: cards, sets, and types.
    Accepts string input deciding which data to return: "cards", "sets", or "types".
    Outputs the fetched data or error message.
    """
    try:
        user_input = agent.receive_parameter('user_input')  # Accepts calls from other nodes
        action = str(user_input).strip().lower()
        
        endpoints = {
            "cards": "https://api.magicthegathering.io/v1/cards",
            "sets": "https://api.magicthegathering.io/v1/sets",
            "types": "https://api.magicthegathering.io/v1/types"
        }
        
        if action not in endpoints:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={
                    'error': f'Invalid input: {action}. Please choose one of: cards, sets, types.'
                }
            )
            return

        response = requests.get(endpoints[action], timeout=10)
        if response.status_code == 200:
            data = response.json()
            agent.send_output(
                agent_output_name='api_response',
                agent_result=data  # JSON is serializable
            )
        else:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={
                    'error': f"API responded with status {response.status_code}",
                    'details': response.text
                }
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': f'Exception occurred: {str(e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='MagicTheGatheringNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
