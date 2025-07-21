from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# D&D 5e API base URL (non-sensitive config, see yml_config)
BASE_URL = "https://www.dnd5eapi.co/api/"
DEFAULT_TIMEOUT = 10

def build_full_url(endpoint: str) -> str:
    if endpoint.startswith('http'):
        return endpoint
    return BASE_URL.rstrip('/') + '/' + endpoint.lstrip('/')

@run_agent
def run(agent: MofaAgent):
    # Add this so other nodes can call it even without meaningful input
    user_input = agent.receive_parameter('user_input')

    # Receive 'operation' parameter to decide which API endpoint to use
    operation = agent.receive_parameter('operation')  # Expects e.g. 'features', 'monster', 'classes'
    endpoint_map = {
        'features': 'features',
        'monster': 'monsters/adult-black-dragon/',
        'classes': 'classes',
    }
    
    if not isinstance(operation, str) or operation not in endpoint_map:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={"error": f"Invalid or missing operation parameter: {operation}"}
        )
        return

    endpoint = endpoint_map[operation]
    url = build_full_url(endpoint)
    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        try:
            result = response.json()
        except Exception as e_json:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={"error": f"Failed to parse response JSON: {str(e_json)}"}
            )
            return
    except requests.RequestException as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={"error": f"API request failed: {str(e)}", "url": url}
        )
        return

    # Output the result (dict, serializable)
    agent.send_output(
        agent_output_name='api_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='DnDApiNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
