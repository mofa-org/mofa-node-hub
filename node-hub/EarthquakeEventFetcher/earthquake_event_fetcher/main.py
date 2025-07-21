from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# You may need to ensure that 'requests' is present in requirements.txt
dependencies = ['requests']

def build_query_url(base_url, params):
    """
    Construct the query URL by appending parameters to the base URL.
    """
    from urllib.parse import urlencode
    return f"{base_url}&{urlencode(params)}"

@run_agent
def run(agent: MofaAgent):
    try:
        # Input Handling
        # All params are received as strings
        params = agent.receive_parameters(['starttime', 'endtime', 'minmagnitude'])
        
        # Validate and type-cast parameters
        query_params = {}
        query_params['starttime'] = str(params.get('starttime', '2023-03-01'))
        query_params['endtime'] = str(params.get('endtime', '2023-03-02'))
        # minmagnitude forced to float string representation
        minmag_raw = params.get('minmagnitude', '5')
        try:
            query_params['minmagnitude'] = str(float(minmag_raw))
        except:
            # Fallback to default if conversion fails
            query_params['minmagnitude'] = '5'

        base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
        # Build request URL with provided parameters
        full_url = build_query_url(base_url, query_params)

        # API Call
        response = requests.get(full_url, timeout=10)
        response.raise_for_status()

        # Validate response is JSON serializable
        data = response.json()
        # output only necessary fields (not raw)
        output_data = {
            'count': data.get('metadata', {}).get('count', 0),
            'earthquakes': [
                {
                    'mag': f.get('properties', {}).get('mag'),
                    'place': f.get('properties', {}).get('place'),
                    'time': f.get('properties', {}).get('time'),
                    'id': f.get('id'),
                }
                for f in data.get('features', [])
            ]
        }
        agent.send_output(
            agent_output_name='earthquake_data',
            agent_result=output_data
        )
    except Exception as e:
        # Error handling; outputs are always serializable
        agent.send_output(
            agent_output_name='earthquake_data',
            agent_result={
                'error': True,
                'message': f'Failed to fetch earthquake data: {str(e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='EarthquakeEventFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
