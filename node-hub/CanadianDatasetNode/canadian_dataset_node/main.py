# Dependency: requests
# Ensure 'requests' is included in your requirements.txt or environment
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No explicit input required for this node as per configuration
    # To facilitate external calls, expect a dummy user_input parameter
    user_input = agent.receive_parameter('user_input')
    
    # Endpoint and request parameter setup
    endpoint = "https://open.canada.ca/data/api/action/package_show"
    params = {"id": "5953da6b-d81b-4a2c-8b27-145892827fb0"}  # Based on config

    try:
        # Make a GET request to the dataset API
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        api_result = response.json()
    except Exception as e:
        # Ensure all errors handled inside the agent
        api_result = {
            "error": True,
            "message": f"Failed to retrieve dataset: {str(e)}"
        }

    # Output must be serializable (dict)
    agent.send_output(
        agent_output_name='canadian_dataset_output',
        agent_result=api_result
    )

def main():
    agent = MofaAgent(agent_name='CanadianDatasetNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
