# Dependencies: requests
# Make sure to add 'requests' to your requirements.txt or installation script.
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive 'type' input parameter. Let user_input enable chaining if not present.
        type_param = agent.receive_parameter('type')
        if not type_param:
            user_input = agent.receive_parameter('user_input')
            type_param = 'meat-and-filler'  # Default fallback from config
        
        # Validate type_param
        allowed_types = ['meat-and-filler', 'all-meat']
        if type_param not in allowed_types:
            agent.send_output(
                agent_output_name='bacon_ipsum_output',
                agent_result={'error': f"Invalid type parameter. Allowed: {allowed_types}", 'input': type_param}
            )
            return
        
        endpoint = f"https://baconipsum.com/api/?type={type_param}"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Output result as stringified list
        agent.send_output(
            agent_output_name='bacon_ipsum_output',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='bacon_ipsum_output',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BaconIpsumNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
