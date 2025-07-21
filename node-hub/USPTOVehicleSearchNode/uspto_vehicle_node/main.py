# Dependencies:
#   - requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    This Agent queries the USPTO IP Marketplace API for vehicles using hardcoded parameter.
    - API Docs: https://developer.uspto.gov/api-catalog?ref=freepublicapis.com
    - Endpoint: https://developer.uspto.gov/ipmarketplace-api/search/query?searchText=vehicles
    - Method: GET
    Input: user_input (ignored but required for dora-rs compatibility)
    Output: 'uspto_vehicle_results' (API JSON or error message)
    """
    # For node composability, still retrieve user_input, but we do not use it
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = "https://developer.uspto.gov/ipmarketplace-api/search/query"
        params = {"searchText": "vehicles"}
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        agent.send_output(
            agent_output_name='uspto_vehicle_results',
            agent_result=data  # Already serializable
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='uspto_vehicle_results',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='USPTOVehicleSearchNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
