from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Add this line for dora-rs dataflow pipeline compatibility
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://randomuser.me/api/', timeout=10)
        response.raise_for_status()
        data = response.json()  # Ensure data can be serialized
    except Exception as e:
        data = {'error': str(e)}
    agent.send_output(
        agent_output_name='random_user_data',
        agent_result=data
    )

def main():
    agent = MofaAgent(agent_name='RandomUserApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests
'''
