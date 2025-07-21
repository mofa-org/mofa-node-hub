from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependency: requests
# Ensure 'requests' is specified in your dependency configuration.

@run_agent
def run(agent: MofaAgent):
    """
    DigimonCardApiNode - dora-rs compliant agent to:
      1. Get a specific Digimon Card by various parameters
      2. Get all Digimon Cards with sorting/filtering

    Input ports:
      - mode: 'search' or 'get_all' (determines which endpoint)
      - params: JSON string with any API request parameters (optional)

    Output ports:
      - api_response: API response (dict or list)
      - api_error: Error information (string/dict)
    """
    try:
        # Required for node linkage (even if not used)
        user_input = agent.receive_parameter('user_input')

        # Main input handling
        mode = agent.receive_parameter('mode')  # 'search' or 'get_all'
        params_json = agent.receive_parameter('params')  # JSON string, can be empty

        # Valid modes
        if mode not in ['search', 'get_all']:
            raise ValueError("mode must be 'search' or 'get_all'")

        # URLs and default params
        endpoints = {
            'search': 'https://digimoncard.io/api-public/search.php',
            'get_all': 'https://digimoncard.io/api-public/getAllCards.php'
        }
        default_params = {
            'search': {
                'n': 'Aldamon', 'desc': 'include a Digimon card', 'color': 'red', 'type': 'digimon',
                'attribute': 'Variable', 'card': 'BT4-016', 'pack': 'BT-04: Booster Great Legend',
                'sort': 'name', 'sortdirection': 'desc', 'series': 'Digimon Card Game',
                'digitype': 'Wizard', 'evocost': '3', 'evocolor': 'Red'
            },
            'get_all': {
                'sort': 'name', 'series': 'Digimon Card Game', 'sortdirection': 'asc'
            }
        }

        # Start with defaults, override from params_json if provided
        try:
            supplied_params = json.loads(params_json) if params_json else {}
            if not isinstance(supplied_params, dict):
                supplied_params = {}
        except Exception:
            supplied_params = {}

        api_params = default_params[mode].copy()
        api_params.update({k: str(v) for k, v in supplied_params.items()})  # All values str

        # Build endpoint and request
        endpoint = endpoints[mode]
        resp = requests.get(endpoint, params=api_params, timeout=20)
        resp.raise_for_status()

        # Try to decode JSON, fallback to raw text
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        agent.send_output(agent_output_name='api_response', agent_result=data)

    except Exception as e:
        # Send full error info for debugging
        agent.send_output(
            agent_output_name='api_error',
            agent_result={
                'error': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='DigimonCardApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()