# Dependencies: requests, python-dotenv
# Install via pip:
#   pip install requests python-dotenv
# .env.secret must set OPENTRIVIA_TOKEN if token access is desired

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env.secret (handled by MOFA framework)
load_dotenv(dotenv_path='.env.secret', override=True)

OPENTRIVIA_ENDPOINT = "https://opentdb.com/api.php"

@run_agent
def run(agent: MofaAgent):
    """
    Receives optional string parameter 'user_token' for authenticated requests. If not provided, defaults to public endpoint.
    Output: trivia_results (dict), keys: 'status', 'results', and optionally 'error'.
    """
    try:
        # Always try to receive a parameter for node interoperability
        user_token = agent.receive_parameter('user_token')
        # Acceptable empty string for no-token path
        use_token = bool(user_token and str(user_token).strip())
    except Exception:
        # No token supplied by caller; default to no-token path
        user_token = None
        use_token = False
    try:
        if use_token:
            token = str(user_token)
            params = {'amount': '10', 'token': token}
        else:
            params = {'amount': '10'}
        response = requests.get(OPENTRIVIA_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()
        trivia_data = response.json()
        output = {
            'status': 'success',
            'results': trivia_data.get('results', []),
            'message': trivia_data.get('response_code', 0)
        }
    except Exception as e:
        output = {
            'status': 'error',
            'results': [],
            'error': str(e)
        }
    agent.send_output(
        agent_output_name='trivia_results',
        agent_result=output
    )

def main():
    agent = MofaAgent(agent_name='OpenTriviaNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
