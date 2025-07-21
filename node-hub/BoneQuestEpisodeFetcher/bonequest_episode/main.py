# Dependencies:
# - requests (pip install requests)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate node linkage by always receiving a dummy input
    user_input = agent.receive_parameter('user_input')
    try:
        # Endpoint configuration
        url = 'https://www.bonequest.com/api/v2/episode/420'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        # Safe error handling and serialization
        data = {'error': True, 'message': str(e)}
    agent.send_output(
        agent_output_name='bonequest_episode',
        agent_result=data
    )

def main():
    agent = MofaAgent(agent_name='BoneQuestEpisodeFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
