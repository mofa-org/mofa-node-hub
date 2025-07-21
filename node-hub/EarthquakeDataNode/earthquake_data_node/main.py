# Dependencies: requests (add to requirements.txt)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameters from framework (all as strings)
        params = agent.receive_parameters(['starttime', 'endtime', 'minmagnitude'])
        
        # Type conversion
        starttime = params.get('starttime', '2023-03-01')  # default if not provided
        endtime = params.get('endtime', '2023-03-02')      # default if not provided
        try:
            minmagnitude = float(params.get('minmagnitude', '5'))
        except Exception:
            minmagnitude = 5.0

        # USGS earthquake API endpoint
        endpoint = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
        query_params = {
            'format': 'geojson',
            'starttime': starttime,
            'endtime': endtime,
            'minmagnitude': minmagnitude
        }

        # Send GET request
        response = requests.get(endpoint, params=query_params, timeout=15)
        response.raise_for_status()
        data = response.json()
        # USGS API always returns geojson/dict

        # Serialize result for output (convert dict to JSON string)
        agent.send_output(
            agent_output_name='earthquake_data',
            agent_result=json.dumps(data)
        )

    except Exception as e:
        # Error containment: output error message as string
        agent.send_output(
            agent_output_name='earthquake_data',
            agent_result=json.dumps({'error': str(e)})
        )

def main():
    agent = MofaAgent(agent_name='EarthquakeDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
