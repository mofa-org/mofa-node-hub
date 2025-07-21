# Dependencies: requests (install via pip if needed)
# No required input parameters, but to support dataflow, accepts 'user_input' as placeholder

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Placeholder to allow connection from other nodes
    user_input = agent.receive_parameter('user_input')
    try:
        # Endpoint 1: Get a user
        resp_user = requests.get('https://api.github.com/users/rails', timeout=15)
        resp_user.raise_for_status()
        user_data = resp_user.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='user_info',
            agent_result={'error': f'Failed to fetch user info: {str(e)}'}
        )
        user_data = None
    if user_data:
        agent.send_output(
            agent_output_name='user_info',
            agent_result=user_data
        )
    try:
        # Endpoint 2: Get a repository
        resp_repo = requests.get('https://api.github.com/repos/rails/rails', timeout=15)
        resp_repo.raise_for_status()
        repo_data = resp_repo.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='repo_info',
            agent_result={'error': f'Failed to fetch repo info: {str(e)}'}
        )
        repo_data = None
    if repo_data:
        agent.send_output(
            agent_output_name='repo_info',
            agent_result=repo_data
        )
    try:
        # Endpoint 3: Get repository content (README.md)
        resp_content = requests.get('https://api.github.com/repos/rails/rails/contents/README.md', timeout=15)
        resp_content.raise_for_status()
        content_data = resp_content.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='repo_content',
            agent_result={'error': f'Failed to fetch repo content: {str(e)}'}
        )
        content_data = None
    if content_data:
        agent.send_output(
            agent_output_name='repo_content',
            agent_result=content_data
        )

def main():
    agent = MofaAgent(agent_name='GithubNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
