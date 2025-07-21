"""
Agent Name: JsonPlaceholderNodeAgent
Module: json_placeholder_node
Description: Fetches post details, all posts, and comments for a post using JSONPlaceholder API. No parameters required for these endpoints.

Dependencies:
- requests
- python-dotenv (if env variables needed)

Dataflow Ports:
- 'post_details'   -> Output for GET https://jsonplaceholder.typicode.com/posts/1
- 'all_posts'      -> Output for GET https://jsonplaceholder.typicode.com/posts
- 'post_comments'  -> Output for GET https://jsonplaceholder.typicode.com/posts/1/comments
"""

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this one by requiring a dummy input (even if not used)
    user_input = agent.receive_parameter('user_input')
    base_url = "https://jsonplaceholder.typicode.com"
    timeout = 30

    endpoints = {
        'post_details': f'{base_url}/posts/1',
        'all_posts': f'{base_url}/posts',
        'post_comments': f'{base_url}/posts/1/comments',
    }

    def fetch_json(url):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {'error': str(e), 'url': url}

    # Get results for each endpoint
    post_details = fetch_json(endpoints['post_details'])
    all_posts = fetch_json(endpoints['all_posts'])
    post_comments = fetch_json(endpoints['post_comments'])

    # Output delivery (all outputs must be serializable)
    agent.send_output(
        agent_output_name='post_details',
        agent_result=post_details
    )
    agent.send_output(
        agent_output_name='all_posts',
        agent_result=all_posts
    )
    agent.send_output(
        agent_output_name='post_comments',
        agent_result=post_comments
    )

def main():
    agent = MofaAgent(agent_name='JsonPlaceholderNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
# Dependencies:
#   requests
#
# Dataflow ports:
#   - 'post_details'
#   - 'all_posts'
#   - 'post_comments'
"""