# Dependencies: requests (install via pip if not already present)
# Environment: None required for open endpoints

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

API_BASE_URL = "https://www.freepublicapis.com/api"
DEFAULT_TIMEOUT = 10
DEFAULT_LIMIT = 10
DEFAULT_SORT = "best"

@run_agent
def run(agent: MofaAgent):
    """
    Supports three operations:
        - Get specific API info: output on 'single_api_info'
        - List APIs: output on 'api_list'
        - Get random API: output on 'random_api_info'
    Operation is selected via 'mode' input. Inputs:
        - mode: one of ['single', 'list', 'random'] (required)
    For mode 'list', can override limit and sort with optional parameters.
    For mode 'single', can pass 'api_id' (string).
    """
    try:
        params = agent.receive_parameters(['mode', 'api_id', 'limit', 'sort', 'user_input'])
        mode = (params.get('mode') or '').strip().lower()
        # user_input always consumed for node chaining (even if unused)
        _ = params.get('user_input')

        if mode not in ['single', 'list', 'random']:
            agent.send_output(agent_output_name='error', agent_result='Invalid "mode". Choose from [single, list, random].')
            return

        if mode == 'single':
            api_id = str(params.get('api_id') or '').strip() or '275'  # Default from example
            url = f"{API_BASE_URL}/apis/{api_id}"
            try:
                resp = requests.get(url, timeout=DEFAULT_TIMEOUT)
                resp.raise_for_status()
                data = resp.json()
                agent.send_output('single_api_info', data)
            except Exception as e:
                agent.send_output('error', f'Error fetching API by id: {api_id}. {str(e)}')

        elif mode == 'list':
            limit = str(params.get('limit') or str(DEFAULT_LIMIT)).strip()
            sort = str(params.get('sort') or DEFAULT_SORT).strip()
            url = f"{API_BASE_URL}/apis?limit={limit}&sort={sort}"
            try:
                resp = requests.get(url, timeout=DEFAULT_TIMEOUT)
                resp.raise_for_status()
                data = resp.json()
                agent.send_output('api_list', data)
            except Exception as e:
                agent.send_output('error', f'Error listing APIs. {str(e)}')

        elif mode == 'random':
            url = f"{API_BASE_URL}/random"
            try:
                resp = requests.get(url, timeout=DEFAULT_TIMEOUT)
                resp.raise_for_status()
                data = resp.json()
                agent.send_output('random_api_info', data)
            except Exception as e:
                agent.send_output('error', f'Error fetching random API. {str(e)}')

    except Exception as err:
        agent.send_output(agent_output_name='error', agent_result=f'Agent error: {str(err)}')

def main():
    agent = MofaAgent(agent_name='FreePublicAPIAggregator')
    run(agent=agent)

if __name__ == '__main__':
    main()
