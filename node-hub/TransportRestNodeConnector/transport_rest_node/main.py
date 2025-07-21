# Dependencies: requests, python-dotenv (for .env.secret loading if needed)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

API_BASE_URL = "https://v6.db.transport.rest"
ENDPOINTS = {
    "stations_with_dblounge": {
        "path": "/stations",
        "params": {"hasDBLounge": "true"},
        "description": "Filter db-stations by hasDBLounge property, get newline-delimited JSON"
    },
    "autocomplete_stations": {
        "path": "/stations",
        "params": {"query": "dammt"},
        "description": "Autocomplete using db-stations-autocomplete"
    },
    "departures_from_halle": {
        "path": "/stops/8010159/departures",
        "params": {"direction": "8011113", "duration": "120"},
        "description": "Halle (Saale) Hbf, in direction Berlin Südkreuz"
    },
}

def call_transport_rest_api(endpoint_key: str) -> dict:
    try:
        endpoint = ENDPOINTS[endpoint_key]
    except KeyError:
        return {"error": f"Invalid endpoint key: {endpoint_key}"}

    url = f"{API_BASE_URL}{endpoint['path']}"
    params = endpoint["params"]
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        try:
            # Attempt to parse JSON per line (newline-delimited JSON)
            content_type = resp.headers.get('Content-Type', '')
            if 'application/x-ndjson' in content_type or ('\n' in resp.text and resp.text.startswith('{')):
                # Split into JSON objects per line
                lines = resp.text.strip().split('\n')
                result = [json.loads(line) for line in lines if line.strip()]
            else:
                result = resp.json()
        except Exception as parse_exc:
            result = {"error": f"Error parsing response: {str(parse_exc)}", "raw_response": resp.text}
    except Exception as e:
        result = {"error": str(e)}
    return result

@run_agent
def run(agent: MofaAgent):
    # Accept endpoint_key from dataflow input, string: one of the allowed endpoint keys
    endpoint_key = agent.receive_parameter('endpoint_key')
    # Optional: allow for easier chaining, even if unused
    user_input = agent.receive_parameter('user_input')
    # Only allow defined endpoints
    result = call_transport_rest_api(endpoint_key)
    try:
        agent.send_output(
            agent_output_name='api_response',
            agent_result=result if isinstance(result, (dict, list, str)) else str(result)
        )
    except Exception as e:
        # Fallback error handling for output
        agent.send_output(
            agent_output_name='api_response',
            agent_result={"error": f"Failed to send output: {str(e)}"}
        )

def main():
    agent = MofaAgent(agent_name='TransportRestNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
