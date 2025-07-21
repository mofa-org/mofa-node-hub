# Dependencies:
#   - requests
# Install with: pip install requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameter: expects IP address as string
        ip = agent.receive_parameter('ip')
        
        # Type check / sanitation
        if not isinstance(ip, str) or ip.strip() == "":
            agent.send_output(
                agent_output_name='greeting_response',
                agent_result={'error': 'Invalid or missing IP address.'}
            )
            return
        # Prepare request
        endpoint = f"https://hellosalut.stefanbohacek.dev/?ip={ip}"
        resp = requests.get(endpoint, timeout=10)
        # Error handling
        if resp.status_code != 200:
            agent.send_output(
                agent_output_name='greeting_response',
                agent_result={
                    'error': f'API call failed with code {resp.status_code}',
                    'details': resp.text
                }
            )
            return
        try:
            data = resp.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='greeting_response',
                agent_result={
                    'error': 'Invalid JSON from API',
                    'details': str(e)
                }
            )
            return
        # Output response
        agent.send_output(
            agent_output_name='greeting_response',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='greeting_response',
            agent_result={
                'error': 'Unhandled exception in Agent',
                'details': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='IpGeolocationGreeterNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
