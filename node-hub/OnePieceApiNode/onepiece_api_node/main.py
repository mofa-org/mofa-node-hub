from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# External Dependencies:
# - requests
# Ensure 'requests' is installed and listed in requirements.txt for deployment.
# No sensitive keys; all endpoints are public as per configuration.

ONEPIECE_ENDPOINTS = {
    "sagas": "https://api.api-onepiece.com/v2/sagas/en",
    "characters": "https://api.api-onepiece.com/v2/characters/en",
    "fruits": "https://api.api-onepiece.com/v2/fruits/en"
}

def fetch_data(endpoint_url: str, timeout: int = 10):
    try:
        resp = requests.get(endpoint_url, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        # Result must be serializable. Return as dict.
        return {"success": True, "data": data}
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@run_agent
def run(agent: MofaAgent):
    # To facilitate calls from other nodes, receive user_input even though not required for this node
    user_input = agent.receive_parameter('user_input')
    # This agent expects a 'resource' parameter specifying what to fetch: 'sagas', 'characters', or 'fruits'.
    resource = agent.receive_parameter('resource')
    # String type enforcement
    resource = str(resource).lower().strip()
    # Validate resource
    if resource not in ONEPIECE_ENDPOINTS:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                "success": False,
                "error": f"Invalid resource: '{resource}'. Choose from {list(ONEPIECE_ENDPOINTS.keys())}."
            }
        )
        return
    endpoint_url = ONEPIECE_ENDPOINTS[resource]
    # Optionally, allow timeout override in seconds via parameter
    timeout_param = agent.receive_parameter('timeout')
    try:
        timeout = int(timeout_param) if timeout_param else 10
    except Exception:
        timeout = 10
    result = fetch_data(endpoint_url, timeout=timeout)
    agent.send_output(
        agent_output_name='api_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='OnePieceApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
