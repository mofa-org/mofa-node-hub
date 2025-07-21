# Dependencies: requests
# To install: pip install requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Dora-rs Agent for fetching space launch data, agencies, or astronauts.
    Input: string 'endpoint_type' - must be one of ['launch_data', 'agencies', 'astronauts']
    Output: JSON dict with the API response or error information.
    """
    # Ensure agent is callable in orchestration
    user_input = agent.receive_parameter('user_input')
    
    try:
        endpoint_type = agent.receive_parameter('endpoint_type')
        # Select endpoint based on input
        endpoint_map = {
            'launch_data': 'https://ll.thespacedevs.com/2.2.0/config/launcher/?format=json',
            'agencies': 'https://ll.thespacedevs.com/2.2.0/agencies/?limit=10&format=json',
            'astronauts': 'https://ll.thespacedevs.com/2.2.0/astronaut/?format=json'
        }
        endpoint_type = str(endpoint_type).strip().lower()
        if endpoint_type not in endpoint_map:
            agent.send_output(
                agent_output_name='spacelaunch_output',
                agent_result={
                    'error': f"Invalid 'endpoint_type': {endpoint_type}. Choose one of: launch_data, agencies, astronauts."
                }
            )
            return
        url = endpoint_map[endpoint_type]
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as e_json:
            agent.send_output(
                agent_output_name='spacelaunch_output',
                agent_result={'error': f'JSON decode error: {str(e_json)}', 'raw': response.text}
            )
            return
        agent.send_output(
            agent_output_name='spacelaunch_output',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='spacelaunch_output',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='SpaceLaunchDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
