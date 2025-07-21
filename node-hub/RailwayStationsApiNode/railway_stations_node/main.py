from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Node configuration (could also be loaded from environment or .env.secret)
DEFAULT_COUNTRY = "ch"
BASE_URL = "https://api.railway-stations.org"
STATION_ID_EXAMPLE = "de/2513"
TIMEOUT = 10

@run_agent
def run(agent: MofaAgent):
    """
    RailwayStationsApiNode - Multi-operation node querying railway-stations.org API
    Input:
        operation: 'stats' | 'by_country' | 'photos_by_id'
        (If operation=='by_country'): country_code
        (If operation=='photos_by_id'): station_id
    Output:
        Dictionary with API response or error message, delivered via 'api_response'
    """
    try:
        params = agent.receive_parameters(['operation', 'country_code', 'station_id'])
        operation = params.get('operation', '').strip().lower()
        country_code = params.get('country_code', DEFAULT_COUNTRY) or DEFAULT_COUNTRY
        station_id = params.get('station_id', STATION_ID_EXAMPLE) or STATION_ID_EXAMPLE

        if operation == 'stats':
            endpoint = f"{BASE_URL}/stats"
            r = requests.get(endpoint, timeout=TIMEOUT)
            r.raise_for_status()
            result = r.json()
        elif operation == 'by_country':
            endpoint = f"{BASE_URL}/photoStationsByCountry/{country_code}"
            r = requests.get(endpoint, timeout=TIMEOUT)
            r.raise_for_status()
            result = r.json()
        elif operation == 'photos_by_id':
            endpoint = f"{BASE_URL}/photoStationById/{station_id}"
            r = requests.get(endpoint, timeout=TIMEOUT)
            r.raise_for_status()
            result = r.json()
        else:
            result = {'error': f'Unknown operation: {operation}. Supported: stats, by_country, photos_by_id'}
    except Exception as e:
        result = {'error': f'API call failed: {str(e)}'}

    agent.send_output(
        agent_output_name='api_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='RailwayStationsApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
