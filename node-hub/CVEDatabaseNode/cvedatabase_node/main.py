from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this node
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = "https://cvedb.shodan.io/cve/CVE-2016-10087"
        resp = requests.get(endpoint, timeout=10)
        try:
            resp.raise_for_status()
        except Exception as e:
            agent.send_output(
                agent_output_name='vuln_info',
                agent_result={
                    'error': f'API returned error: {str(e)}',
                    'status_code': resp.status_code
                }
            )
            return
        try:
            vuln_data = resp.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='vuln_info',
                agent_result={
                    'error': 'Failed to parse response as JSON',
                    'details': str(e)
                }
            )
            return
        agent.send_output(
            agent_output_name='vuln_info',
            agent_result=vuln_data # Must be serializable; resp.json() returns dict
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='vuln_info',
            agent_result={
                'error': 'Unhandled exception',
                'details': str(ex)
            }
        )

def main():
    agent = MofaAgent(agent_name='CVEDatabaseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
