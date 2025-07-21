# Dependencies:
#   - requests
#
# [Install] pip install requests
# .env.secret may be used for environment variable(s) if future API keys are required, but none needed here.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive all necessary parameters as strings
        params = agent.receive_parameters(['latitude', 'longitude', 'hourly'])  # expects: { 'latitude': '...', 'longitude': '...', 'hourly': '...' }
        # Convert to appropriate types
        lat = float(params['latitude'])
        lon = float(params['longitude'])
        # 'hourly' can be a comma-separated list in string form
        pollen_types = [p.strip() for p in params['hourly'].split(',') if p.strip()]
        # Construct API request
        endpoint = 'https://air-quality-api.open-meteo.com/v1/air-quality'
        query_params = {
            'latitude': lat,
            'longitude': lon,
            'hourly': ','.join(pollen_types)
        }
        # Make GET request with timeout and retry logic
        session = requests.Session()
        retries = 2
        last_err = None
        for attempt in range(retries + 1):
            try:
                response = session.get(endpoint, params=query_params, timeout=10)
                response.raise_for_status()
                result = response.json()  # Should be dict
                # Sanity check output serialization
                if not isinstance(result, (dict, list, str)):
                    agent.send_output('pollen_forecast', str(result))
                else:
                    agent.send_output('pollen_forecast', result)
                return
            except Exception as e:
                last_err = str(e)
        # If all attempts failed
        agent.send_output('pollen_forecast', {'error': 'Failed to fetch pollen data', 'detail': last_err})
    except Exception as ex:
        agent.send_output('pollen_forecast', {'error': 'Agent internal error', 'detail': str(ex)})

def main():
    agent = MofaAgent(agent_name='PollenForecastNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
