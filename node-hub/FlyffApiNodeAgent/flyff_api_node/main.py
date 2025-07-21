# Dependencies: requests, python-dotenv (for handling .env if needed)
# You must ensure requests is installed and available in the agent environment
def _build_full_url(base_url: str, path: str) -> str:
    if base_url.endswith('/') and path.startswith('/'):
        return base_url[:-1] + path
    elif not base_url.endswith('/') and not path.startswith('/'):
        return base_url + '/' + path
    else:
        return base_url + path

import requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent

# Stateless; config defined here for demo purposes. Production: move to config file!
FLYFF_API_BASE_URL = "https://api.flyff.com/"
ENDPOINTS = {
    'get_all_class_ids': '/class',
    'get_class_764': '/class/764',
    'get_all_world_ids': '/world',
    'get_world_6063': '/world/6063',
}
TIMEOUT = 30
RETRIES = 3

@run_agent
def run(agent: MofaAgent):
    """
    Receives two string parameters:
      - endpoint_name: one of get_all_class_ids, get_class_764, get_all_world_ids, get_world_6063
      - user_input: dummy (to help with dataflow, per spec)
    """
    try:
        # Input handling: both as strings (dora-rs compliance)
        params = agent.receive_parameters(['endpoint_name', 'user_input'])
        endpoint_name = params.get('endpoint_name', '').strip()
        # user_input can be ignored, used for facilitating dataflow

        if endpoint_name not in ENDPOINTS:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={
                    'error': f"Unknown endpoint_name '{endpoint_name}'. Must be one of: {list(ENDPOINTS.keys())}",
                    'success': False
                }
            )
            return

        url = _build_full_url(FLYFF_API_BASE_URL, ENDPOINTS[endpoint_name])

        # Retry logic
        last_exc = None
        for attempt in range(RETRIES):
            try:
                response = requests.get(url, timeout=TIMEOUT)
                response.raise_for_status()
                data = response.json()
                agent.send_output(
                    agent_output_name='api_response',
                    agent_result=data if isinstance(data, (dict, list)) else str(data)
                )
                return
            except Exception as e:
                last_exc = str(e)
                continue
        # If all attempts fail
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': f"Request to {url} failed after {RETRIES} attempts: {last_exc}",
                'success': False
            }
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': f"Agent error: {str(e)}",
                'success': False
            }
        )

def main():
    agent = MofaAgent(agent_name='FlyffApiNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()
