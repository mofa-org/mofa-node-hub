from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # For dora-rs interface compliance; required to allow other nodes to provide input if needed.
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://api.ipty.org', timeout=10)
        response.raise_for_status()
        # Response is plain text with IP or may be JSON with network data, try to parse
        try:
            data = response.json()
        except ValueError:
            data = {'ip': response.text.strip()}
        agent.send_output(
            agent_output_name='ip_info',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='ip_info',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='NetworkIpAddressNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
