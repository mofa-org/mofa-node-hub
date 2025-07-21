# Dependency requirements:
#   requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://teehee.dev/api/joke', timeout=10)
        response.raise_for_status()
        joke_data = response.json()
        # Ensure only serializable fields are returned
        serializable_data = {
            'id': str(joke_data.get('id', '')),
            'question': joke_data.get('question', ''),
            'answer': joke_data.get('answer', ''),
            'permalink': joke_data.get('permalink', '')
        }
        agent.send_output(
            agent_output_name='joke_data',
            agent_result=serializable_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='joke_data',
            agent_result={
                'error': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='TeeheeJokeRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
