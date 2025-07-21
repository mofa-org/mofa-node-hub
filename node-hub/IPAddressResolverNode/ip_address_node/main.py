from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # For compliance, always receive user_input even if not required (to facilitate chaining)
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://api.aruljohn.com/ip/json', timeout=10)
        response.raise_for_status()
        # The API returns JSON -- ensure output is serializable
        ip_info = response.json()
        # Defensive: ensure dict for serialization
        if not isinstance(ip_info, dict):
            raise ValueError('Unexpected API response format')
        agent.send_output(
            agent_output_name='ip_info',
            agent_result=ip_info
        )
    except Exception as e:
        # Contain all errors, return as dict
        agent.send_output(
            agent_output_name='ip_info',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='IPAddressResolverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
