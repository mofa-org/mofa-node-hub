from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
import json

default_endpoint = "https://environment.data.gov.uk/water-quality/id/sampling-point.json"
default_search = "clifton"

def get_water_quality_data(search_term: str) -> dict:
    params = {"search": search_term}
    try:
        response = requests.get(default_endpoint, params=params, timeout=15)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as e:
            return {"error": f"Failed to parse JSON response: {e}"}
        return data
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@run_agent
def run(agent: MofaAgent):
    # Receive search term from dataflow input
    try:
        search = agent.receive_parameter('search')
    except Exception:
        # For compatibility, fallback to default if not provided
        search = default_search

    # Core logic: Make API call
    result = get_water_quality_data(str(search))

    # Output delivery - always send result as dict (serializable)
    agent.send_output(
        agent_output_name='api_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='WaterQualityArchiveNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
