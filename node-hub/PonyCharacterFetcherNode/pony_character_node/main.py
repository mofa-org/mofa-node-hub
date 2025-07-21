# Dependencies: requests
# You must ensure the 'requests' package is available in your deployment environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate upstream compatibility even if no input required
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://ponyapi.net/v1/character/all', timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as json_err:
            agent.send_output(
                agent_output_name='pony_characters',
                agent_result={
                    'error': True,
                    'message': f'Failed to parse JSON: {str(json_err)}'
                }
            )
            return
        agent.send_output(
            agent_output_name='pony_characters',
            agent_result=data if isinstance(data, (dict, list)) else {'data': str(data)}
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='pony_characters',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='PonyCharacterFetcherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
