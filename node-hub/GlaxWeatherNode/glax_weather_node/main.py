from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    """
    GlaxWeatherNode: Calls the glax_weather public API to retrieve current or hourly weather data for a given location.
    Inputs (all as str): 'location', 'lon', 'lat', 'units', 'forecast'.
    Output: Dict with API response, sent on 'weather_response' port.
    """
    try:
        # Receive all parameters as string (use defaults if not provided)
        params = agent.receive_parameters(['location', 'lon', 'lat', 'units', 'forecast'])
        
        # Set API endpoint and defaults (from config; override if you want to make configurable by input)
        base_url = "https://dragon.best/api/glax_weather.json"

        # Use config/yml defaults if parameters are empty
        defaults = {
            'location': '',
            'lon': '46.9481',
            'lat': '7.4474',
            'units': 'metric',
            'forecast': 'on',
        }
        
        # Merge params with defaults (input param wins if not empty)
        query = {}
        for k in defaults:
            v = params.get(k, '').strip()
            query[k] = v if v else defaults[k]

        # Forecast flag logic: if forecast is missing or off, just get current weather
        forecast_val = query.get('forecast', 'on').lower()
        if forecast_val in ['on', 'true', '1', 'yes']:
            query['forecast'] = 'on'
        else:
            # Remove forecast parameter for current-only weather (API design)
            query.pop('forecast', None)

        response = requests.get(base_url, params=query, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Output through dataflow port 'weather_response'
        agent.send_output(
            agent_output_name='weather_response',
            agent_result=data
        )
    except Exception as e:
        # Always output a meaningful error in a serializable dictionary form
        agent.send_output(
            agent_output_name='weather_response',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='GlaxWeatherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
