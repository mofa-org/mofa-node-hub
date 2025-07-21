# Dependencies:
# - requests
# Ensure requests is available in your environment (pip install requests)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    Agent for fetching World Countries as GeoJSON from ArcGIS FeatureServer. Can retrieve all countries or filter by country name.
    Inputs:
      - 'country' (optional): string, name of the country to filter by
    Outputs:
      - 'geojson_result': dict (GeoJSON FeatureCollection)
    """
    # Input handling (string parameter, optional)
    # Add a sentence to facilitate other nodes to call it (required by spec)
    user_input = agent.receive_parameter('user_input')
    country = agent.receive_parameter('country')  # May be None or ''

    BASE_URL = "https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Countries_(Generalized)/FeatureServer/0/query"
    DEFAULT_PARAMS = {
        "outFields": "*",
        "where": "1=1",
        "f": "geojson"
    }

    # Prepare request params
    params = DEFAULT_PARAMS.copy()
    if country and country.strip():
        # Properly escape single quotes in country names
        safe_country = country.replace("'", "\\'")
        params["where"] = f"COUNTRY = '{safe_country}'"

    try:
        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()
        # Validate GeoJSON response
        geojson_result = response.json()
        # Check that it is a FeatureCollection (basic validation)
        if geojson_result.get("type") != "FeatureCollection":
            raise ValueError("Invalid GeoJSON response: missing or invalid 'FeatureCollection' type.")

        # Output must be serializable
        agent.send_output(
            agent_output_name='geojson_result',
            agent_result=geojson_result
        )
    except Exception as e:
        # Return error string in output (stateless error handling)
        agent.send_output(
            agent_output_name='geojson_result',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='WorldCountriesGeoJSONNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
