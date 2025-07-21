from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call (required by interface)
    user_input = agent.receive_parameter('user_input')
    
    ip_services = [
        'https://api64.ipify.org?format=json',
        'https://api.ipify.org?format=json'
    ]
    public_ip_response = None
    error_msgs = []

    for endpoint in ip_services:
        try:
            resp = requests.get(endpoint, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                # Validate presence of 'ip' field and valid string
                if isinstance(data, dict) and 'ip' in data and isinstance(data['ip'], str):
                    public_ip_response = {'ip': data['ip'], 'source': endpoint}
                    break
                else:
                    error_msgs.append(f"Malformed response from {endpoint}: {data}")
            else:
                error_msgs.append(f"HTTP {resp.status_code} from {endpoint}")
        except Exception as e:
            error_msgs.append(f"Exception from {endpoint}: {str(e)}")

    if public_ip_response:
        agent.send_output(
            agent_output_name='public_ip',
            agent_result=public_ip_response  # dict is serializable
        )
    else:
        agent.send_output(
            agent_output_name='public_ip',
            agent_result={
                'error': 'Unable to fetch public IP from all endpoints.',
                'details': error_msgs
            }
        )

def main():
    agent = MofaAgent(agent_name='PublicIPNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
