# Dependencies: requests, python-dotenv (for env var management)
# Export this agent as sports_data_node.py

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file (especially for API KEY)
load_dotenv()

BASE_URL = os.getenv('THESPORTSDB_BASE_URL', 'https://www.thesportsdb.com/api/v1/json/3/')
API_KEY = os.getenv('THESPORTSDB_API_KEY', 'your_thesportsdb_api_key_here')
TIMEOUT = int(os.getenv('THESPORTSDB_TIMEOUT', '10'))
RETRIES = int(os.getenv('THESPORTSDB_RETRIES', '3'))

SUPPORTED_ENDPOINTS = {
    'search_event': {
        'path': 'searchevents.php',
        'required_params': ['e', 's'],
        'description': 'Search for event by event name',
        'output': 'event_data',
    },
    'all_leagues': {
        'path': 'all_leagues.php',
        'required_params': [],
        'description': 'List all leagues',
        'output': 'league_list',
    },
    'search_player': {
        'path': 'searchplayers.php',
        'required_params': ['p'],
        'description': 'Search for players by name',
        'output': 'player_data',
    },
    'search_teams': {
        'path': 'search_all_teams.php',
        'required_params': ['s', 'c'],
        'description': 'List all teams in a country/league',
        'output': 'teams_info',
    },
    'all_countries': {
        'path': 'all_countries.php',
        'required_params': [],
        'description': 'List all countries',
        'output': 'countries',
    },
}


def make_request(endpoint_path, params=None):
    url = BASE_URL.rstrip('/') + '/' + endpoint_path
    # Always add api key, even if it is the demo one
    params = params or {}
    if API_KEY and '3/' in url:  # avoid duplicate if demo key
        pass  # When using demo key, its a public GET
    try:
        for attempt in range(RETRIES):
            resp = requests.get(url, params=params, timeout=TIMEOUT)
            if resp.status_code == 200:
                try:
                    return resp.json()
                except Exception as e:
                    return {'error': 'Failed to parse JSON', 'detail': str(e)}
            # Try again on next loop if not 200
        return {'error': f'Request failed after {RETRIES} tries', 'url': url, 'params': params}
    except Exception as ex:
        return {'error': 'Request exception', 'detail': str(ex)}

@run_agent
def run(agent: MofaAgent):
    """
    SportsDataApiNode - fetches sports data from TheSportsDB public API.
    """
    # Stateless pattern: receive operation name and parameter(s) as plain strings
    op = agent.receive_parameter('operation')  # Name of API function to use
    # For maximal compatibility (for chaining), always provide user_input
    user_input = agent.receive_parameter('user_input')
    # Gather the required parameters dynamically per supported API
    params_dict = {}
    try:
        op = str(op).strip().lower()
        matched = None
        for k, v in SUPPORTED_ENDPOINTS.items():
            if op == k or op == v['path'].replace('.php', ''):
                matched = v
                endpoint_key = k
                break
        if not matched:
            agent.send_output(agent_output_name='error', agent_result={'error': f'Invalid operation: {op}'})
            return
        # Collect parameters
        if matched['required_params']:
            # Receive_parameters as JSON encoded dict via string
            params_string = agent.receive_parameter('params_json')
            try:
                import json
                raw = json.loads(params_string) if params_string else {}
                for param_name in matched['required_params']:
                    if param_name not in raw:
                        agent.send_output(agent_output_name='error', agent_result={
                            'error': f'Missing required parameter: {param_name}',
                            'expected_params': matched['required_params']
                        })
                        return
                    params_dict[param_name] = raw[param_name]
            except Exception as parse_error:
                agent.send_output(agent_output_name='error', agent_result={'error': 'Invalid JSON in params_json', 'detail': str(parse_error)})
                return
        result = make_request(matched['path'], params_dict)
        if 'error' in result:
            agent.send_output(agent_output_name='error', agent_result=result)
        else:
            agent.send_output(agent_output_name=matched['output'], agent_result=result)
    except Exception as ex:
        agent.send_output(agent_output_name='error', agent_result={'error': 'Internal Agent Error', 'detail': str(ex)})

def main():
    agent = MofaAgent(agent_name='SportsDataApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
