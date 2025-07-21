# Dependencies: requests
# Ensure you have 'requests' installed in your environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
from urllib.parse import urlencode

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive mandatory input to facilitate chaining, even if not needed
        user_input = agent.receive_parameter('user_input')

        # Determine operation type based on optional parameter 'operation'
        operation = agent.receive_parameter('operation')  # string: 'search_city', 'details', 'reverse'

        base_url = "https://nominatim.openstreetmap.org"
        endpoints = {
            'search_city': '/search.php',
            'details': '/details',
            'reverse': '/reverse'
        }
        default_format = 'jsonv2'
        output = {}

        # Use operation to choose endpoint & parameters
        if operation == 'search_city':
            # expects 'city' (optional; default 'bern')
            city = agent.receive_parameter('city') or 'bern'
            params = {'city': city, 'format': default_format}
            endpoint = endpoints['search_city']
        elif operation == 'details':
            # expects 'osmtype' (optional; default 'R'), 'osmid' (optional; default 175905), 'format' (optional)
            osmtype = agent.receive_parameter('osmtype') or 'R'
            osmid_str = agent.receive_parameter('osmid') or '175905'
            format_type = agent.receive_parameter('format') or 'json'
            try:
                osmid = int(osmid_str)
            except Exception:
                osmid = 175905
            params = {'osmtype': osmtype, 'osmid': osmid, 'format': format_type}
            endpoint = endpoints['details']
        elif operation == 'reverse':
            # expects 'lat', 'lon', 'zoom' (all optional)
            lat = agent.receive_parameter('lat') or '40.7127281'
            lon = agent.receive_parameter('lon') or '-74.0060152'
            zoom = agent.receive_parameter('zoom') or '10'
            format_type = agent.receive_parameter('format') or 'json'
            params = {'lat': lat, 'lon': lon, 'zoom': zoom, 'format': format_type}
            endpoint = endpoints['reverse']
        else:
            # Default: search for city Bern
            params = {'city': 'bern', 'format': default_format}
            endpoint = endpoints['search_city']

        url = f"{base_url}{endpoint}?{urlencode(params)}"

        try:
            response = requests.get(url, headers={'User-Agent': 'MofaGeocodingAgent/1.0'})
            response.raise_for_status()
            output = response.json()
        except Exception as e:
            output = {'error': True, 'message': str(e), 'tried_url': url}

        # Ensure output is serializable (dict or list)
        agent.send_output(
            agent_output_name='geocoding_result',
            agent_result=output
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='geocoding_result',
            agent_result={'error': True, 'message': f'Unexpected agent error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='NominatimGeocodingNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
