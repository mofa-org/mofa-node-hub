from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    """
    Dora-rs compliant agent for accessing Civitai API models/images endpoints with sfw filtering.
    Inputs:
        - entity_type: str ['models' or 'images'] (required)
        - limit: str (optional, overrides default)
        - nsfw: str (optional, overrides default)
    Output:
        - civitai_api_response: dict (API JSON response or error message)
    """
    try:
        # Required input to facilitate call from other nodes, even if unused
        user_input = agent.receive_parameter('user_input')
        
        # Receive parameters, default if not provided
        params = agent.receive_parameters(['entity_type', 'limit', 'nsfw'])
        entity_type = params.get('entity_type', '').strip().lower()  # must be 'models' or 'images'
        
        # Default values from config
        api_base_url = os.getenv('CIVITAI_API_BASE_URL', 'https://civitai.com/api/v1')
        default_limit = '10'
        default_nsfw = 'none'
        
        # Endpoint selection
        if entity_type not in ('models', 'images'):
            result = {'error': 'Invalid or missing entity_type. Must be "models" or "images".'}
            agent.send_output('civitai_api_response', result)
            return
        endpoint = f"{api_base_url}/{entity_type}"
        
        # Parameter management (all must be string)
        limit = params.get('limit') if params.get('limit') else default_limit
        nsfw = params.get('nsfw') if params.get('nsfw') else default_nsfw
        query_params = {'limit': str(limit), 'nsfw': str(nsfw)}
        
        # HTTP GET
        try:
            response = requests.get(endpoint, params=query_params, timeout=10)
            response.raise_for_status()
            api_result = response.json()
        except Exception as e:
            api_result = {'error': f"API request failed: {str(e)}"}
        
        # Output serialization check
        if not isinstance(api_result, (dict, list, str)):
            api_result = {'error': 'API result not serializable!'}
        agent.send_output('civitai_api_response', api_result)
    except Exception as ex:
        # Top-level error containment
        error_message = {'error': f"Agent exception: {str(ex)}"}
        agent.send_output('civitai_api_response', error_message)

def main():
    agent = MofaAgent(agent_name='CivitaiApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
