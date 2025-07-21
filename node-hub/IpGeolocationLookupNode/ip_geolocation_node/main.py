from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameter (IP address as string)
        ip = agent.receive_parameter('ip')
        if not isinstance(ip, str) or not ip:
            raise ValueError('Input parameter "ip" must be a non-empty string.')
        
        # Call IP2Location API
        endpoint = f'https://api.ip2location.io/?ip={ip}'
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Ensure serializability
        if not isinstance(data, dict):
            raise ValueError('API response is not a valid dictionary.')
        
        agent.send_output(
            agent_output_name='geolocation_result',
            agent_result=data
        )
    except Exception as e:
        # Error containment: deliver error info in output
        agent.send_output(
            agent_output_name='geolocation_result',
            agent_result={
                'error': True,
                'error_message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='IpGeolocationLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
