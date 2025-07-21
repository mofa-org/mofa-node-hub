# Dependencies: requests
# Make sure 'requests' is specified in your package dependency configuration (e.g., requirements.txt)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

API_ENDPOINTS = {
    'rainfall': 'https://api-open.data.gov.sg/v2/real-time/api/rainfall',
    'uv': 'https://api-open.data.gov.sg/v2/real-time/api/uv',
    'forecast': 'https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast'
}

def fetch_data_from_api(endpoint_url):
    try:
        response = requests.get(endpoint_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {'error': True, 'message': str(e)}

@run_agent
def run(agent: MofaAgent):
    # No input required, but facilitate pipeline integration
    user_input = agent.receive_parameter('user_input')  # Accept dummy input if linked nodes exist
    
    # Select which data to fetch (default: all)
    # If specific type is desired, accept a 'data_type' parameter
    data_type = agent.receive_parameter('data_type') if 'data_type' in (agent.input_config or {}) else None

    results = {}
    
    if data_type and data_type in API_ENDPOINTS:
        results[data_type] = fetch_data_from_api(API_ENDPOINTS[data_type])
    else:
        # Fetch all data endpoints
        for key, url in API_ENDPOINTS.items():
            results[key] = fetch_data_from_api(url)

    # Output results (will always be serializable dict)
    agent.send_output(
        agent_output_name='singapore_weather_data',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='SingaporeWeatherApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
