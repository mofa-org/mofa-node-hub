from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate proper node connections, always check for 'user_input', even if not used
    user_input = agent.receive_parameter('user_input')
    
    ip_address = '127.0.0.1'  # Hardcoded per configuration
    url = f'https://www.baguette-radar.com/api/ip/{ip_address}'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # The API returns JSON; validate serializability
        result = response.json()
    except Exception as e:
        # Full error containment, return error message in output
        result = {'error': True, 'message': str(e)}

    agent.send_output(
        agent_output_name='vpn_proxy_check_result',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='IpVpnProxyCheckerNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests
'''
