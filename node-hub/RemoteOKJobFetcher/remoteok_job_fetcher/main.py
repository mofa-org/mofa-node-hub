from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # For compatibility in dataflow: receive a user input (not used, but required by framework)
        user_input = agent.receive_parameter('user_input')
        api_url = "https://remoteok.com/api"
        response = requests.get(api_url, timeout=15)
        if response.status_code != 200:
            agent.send_output(
                agent_output_name='job_fetch_error',
                agent_result={
                    'error': True,
                    'message': f"Request failed with status code {response.status_code}"
                }
            )
            return
        # The API sometimes returns JSON with leading garbage text; filter that if present
        try:
            jobs_data = response.json()
        except Exception as e:
            # Try to fix: skip lines before first valid array/
            import json
            content = response.text.strip()
            try:
                jobs_data = json.loads(content[content.find('['):])
            except Exception as inner_exc:
                agent.send_output(
                    agent_output_name='job_fetch_error',
                    agent_result={
                        'error': True,
                        'message': f"JSON parse failed: {str(inner_exc)}"
                    }
                )
                return
        agent.send_output(
            agent_output_name='remoteok_jobs',
            agent_result=jobs_data  # List of jobs (serializable)
        )
    except Exception as exc:
        agent.send_output(
            agent_output_name='job_fetch_error',
            agent_result={
                'error': True,
                'message': str(exc)
            }
        )

def main():
    agent = MofaAgent(agent_name='RemoteOKJobFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
