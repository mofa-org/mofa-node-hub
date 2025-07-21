# Dependencies: requests
# If using this agent, ensure 'requests' package is available.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    Nexarda Search Node Agent
    Searches NEXARDA™ for video games and related entities using the public API.
    Input:
        - query (str): The game search query to send to NEXARDA (defaults to 'Example Game')
    Output:
        - search_results (dict/list/str): The results from the NEXARDA API
    """
    try:
        # Accept user input for search query. If none provided, use default.
        user_query = agent.receive_parameter('query')  # Always expect as string
        if not user_query or user_query.strip() == '':
            user_query = 'Example Game'
        # Prepare request
        base_url = 'https://www.nexarda.com/api/v3/search'
        params = {
            'type': 'games',
            'q': user_query,
        }
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        # Try to parse JSON; if not possible, just return text
        try:
            data = response.json()
        except Exception:
            data = response.text
        # Ensure serialization
        if not isinstance(data, (str, dict, list)):
            data = str(data)
        agent.send_output(
            agent_output_name='search_results',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='search_results',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='NexardaSearchNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
