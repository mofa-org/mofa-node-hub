from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitates input compatibility even if there is no user input required
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://picsum.photos/v2/list')
        response.raise_for_status()
        # Ensure serialization
        data = response.json()
        agent.send_output(
            agent_output_name='picsum_photos_list',
            agent_result=data
        )
    except Exception as e:
        # Output error information as a serializable string
        agent.send_output(
            agent_output_name='picsum_photos_list',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='PicsumPhotosNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests
- mofa (e= your Dora-rs Python SDK)
'''
