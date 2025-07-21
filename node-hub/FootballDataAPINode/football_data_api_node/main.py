from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# Documentation: https://www.football-data.org/documentation/quickstart?ref=freepublicapis.com
# Dependencies: requests

@run_agent
def run(agent: MofaAgent):
    """
    FootballDataAPINode retrieves football competitions data from Football Data API.
    Input: user_input (str, optional, ignored but required for compliance)
    Output: competitions_data (list/dict/str) - competitions data from the API
    """
    # To facilitate chain call; input is not used but required for node compatibility
    user_input = agent.receive_parameter('user_input')
    try:
        api_url = 'https://api.football-data.org/v4/competitions/'
        api_key = os.getenv('FOOTBALL_DATA_API_KEY')
        if not api_key:
            raise ValueError('Missing FOOTBALL_DATA_API_KEY in environment')

        headers = {
            'X-Auth-Token': api_key,
        }
        timeout = 30  # Default timeout, can be customized
        response = requests.get(api_url, headers=headers, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        # Ensure result is serializable
        agent.send_output(
            agent_output_name='competitions_data',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='competitions_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='FootballDataAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()
