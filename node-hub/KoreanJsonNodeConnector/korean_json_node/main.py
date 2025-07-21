from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Fetches data from one of the Korean JSON public APIs: todos, comments, users, or posts.
    Expects a string input specifying which resource to fetch: one of 'todos', 'comments', 'users', or 'posts'.
    Output is sent to the corresponding dataflow port named 'korean_json_output'.
    """
    # Input: resource type selection
    resource_type = agent.receive_parameter('resource_type')
    
    # Validate and map resource type
    resource_map = {
        'todos': 'https://koreanjson.com/todos',
        'comments': 'https://koreanjson.com/comments',
        'users': 'https://koreanjson.com/users',
        'posts': 'https://koreanjson.com/posts',
    }
    url = resource_map.get(resource_type.strip().lower())
    if url is None:
        agent.send_output(
            agent_output_name='korean_json_output',
            agent_result={
                'error': True,
                'message': f"Invalid resource_type '{resource_type}'. Please choose from 'todos', 'comments', 'users', or 'posts'."
            }
        )
        return
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        agent.send_output(
            agent_output_name='korean_json_output',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='korean_json_output',
            agent_result={
                'error': True,
                'message': f'API request failed: {str(e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='KoreanJsonNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
  - requests

How to install: pip install requests

Input Port:
  - resource_type (str): 'todos', 'comments', 'users', or 'posts'
Output Port:
  - korean_json_output (list or dict): API response or error object
"""