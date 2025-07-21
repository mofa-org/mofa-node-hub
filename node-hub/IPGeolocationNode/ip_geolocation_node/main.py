from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate calls from other nodes, receive a dummy user_input parameter
    user_input = agent.receive_parameter('user_input')
    
    api_url = 'https://api.country.is/9.9.9.9'

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure the output is serializable
        output_result = data if isinstance(data, (dict, list, str)) else str(data)
        agent.send_output(
            agent_output_name='geolocation_info',
            agent_result=output_result
        )
    except Exception as e:
        # Handle all errors within the Agent boundaries
        agent.send_output(
            agent_output_name='geolocation_info',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='IpGeolocationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
