# Dependencies: requests
# Ensure 'requests' is listed in your runtime dependencies.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    This agent retrieves information from the EVE Online ESI API — specifically universe structures,
    market prices, and regions. No user input is required, but a placeholder receive_parameter is included
    for dataflow consistency: user_input = agent.receive_parameter('user_input')
    Outputs:
        - structures: List/dict of universe structures info
        - market_prices: List of market prices
        - regions: List/dict of region info
    """
    # Placeholder for framework compliance when no input is required
    user_input = agent.receive_parameter('user_input')
    BASE_URL = "https://esi.evetech.net/latest"
    endpoints = {
        "structures": "/universe/structures/",
        "market_prices": "/markets/prices/",
        "regions": "/universe/regions/"
    }
    headers = {"Accept": "application/json"}
    results = {}

    for key, endpoint in endpoints.items():
        try:
            response = requests.get(BASE_URL + endpoint, headers=headers, timeout=10)
            response.raise_for_status()
            # Attempt to parse JSON response. If it fails, send error message
            try:
                results[key] = response.json()
            except Exception as e:
                results[key] = {"error": f"Failed to parse JSON for {key}: {str(e)}"}
        except requests.RequestException as e:
            results[key] = {"error": f"Request to {endpoint} failed: {str(e)}"}

    # Output each result to its own port for clear dataflow
    for key, value in results.items():
        agent.send_output(agent_output_name=key, agent_result=value)

def main():
    agent = MofaAgent(agent_name='EveOnlineUniverseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()