# Dependencies:
#   - requests
#
# This agent fetches the latest SpaceX launch data from the SpaceX API and outputs the results as a dict.
# Input: receives 'user_input' parameter for orchestration compatibility (ignored in logic)
# Output port: 'launch_data'

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate orchestration, even if unused
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://api.spacexdata.com/v5/launches/latest', timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure the output is serializable (dict)
        agent.send_output(agent_output_name='launch_data', agent_result=data)
    except Exception as e:
        # Error handling: send error string to the same output port
        agent.send_output(agent_output_name='launch_data', agent_result={'error': str(e)})

def main():
    agent = MofaAgent(agent_name='SpaceXLaunchDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
