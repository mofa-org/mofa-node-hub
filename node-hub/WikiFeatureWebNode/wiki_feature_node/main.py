# Dependencies: requests
# If not present, add requests to your requirements.txt or pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

WIKI_ENDPOINT = "https://en.wikipedia.org/w/api.php"
DEFAULT_PARAMS = {
    'action': 'query',
    'prop': 'revisions',
    'titles': 'bird',
    'rvprop': 'content',
    'format': 'json'
}

@run_agent
def run(agent: MofaAgent):
    """
    WikiFeatureWebNode Agent
    Fetches content for a predefined Wikipedia page ('bird') using MediaWiki API.
    Receives optional input parameter 'titles' (Wikipedia page title, str).
    Outputs:
        - 'wiki_content': dict (MediaWiki JSON response)
        - 'error': str (error message if any)
    """
    try:
        # To facilitate node calls even if no input needed for default, receive an optional user input
        user_input = agent.receive_parameter('user_input')  # Unused, placeholder for dataflow compliance
        # Optionally allow title override; otherwise defaults to 'bird'
        title = agent.receive_parameter('titles') if 'titles' in agent._config.get('request_parameter', {}) else None
        params = DEFAULT_PARAMS.copy()
        if title is not None and title.strip():
            params['titles'] = title.strip()
        response = requests.get(WIKI_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()
        # Ensure output is serializable
        agent.send_output(
            agent_output_name='wiki_content',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result=str(e)
        )

def main():
    agent = MofaAgent(agent_name='WikiFeatureWebNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
