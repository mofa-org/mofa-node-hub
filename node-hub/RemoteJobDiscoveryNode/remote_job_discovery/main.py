from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependency: requests (install via pip if not present)
# API documentation: https://jobicy.com/jobs-rss-feed?ref=freepublicapis.com

@run_agent
def run(agent: MofaAgent):
    try:
        # Gather input parameters (facilitates chaining by always accepting 'user_input')
        user_input = agent.receive_parameter('user_input')  # to enable other nodes to pass input
        count = agent.receive_parameter('count')
        geo = agent.receive_parameter('geo')
        industry = agent.receive_parameter('industry')
        tag = agent.receive_parameter('tag')

        # Parameter sanitization and defaulting
        try:
            count_value = int(count) if count is not None else 20
        except Exception:
            count_value = 20
        geo_value = geo if geo else 'usa'
        industry_value = industry if industry else 'marketing'
        tag_value = tag if tag else 'seo'

        base_url = 'https://jobicy.com/api/v2/remote-jobs'
        params = {
            'count': count_value,
            'geo': geo_value,
            'industry': industry_value,
            'tag': tag_value
        }

        try:
            response = requests.get(base_url, params=params, timeout=8)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='remote_job_results',
                agent_result={
                    'error': 'Failed to fetch jobs',
                    'details': str(e)
                }
            )
            return

        # Ensure serialization (dict or list)
        agent.send_output(
            agent_output_name='remote_job_results',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='remote_job_results',
            agent_result={
                'error': 'Agent failure',
                'details': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='RemoteJobDiscoveryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
