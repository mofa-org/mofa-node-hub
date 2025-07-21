from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependencies:
# - requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameters as strings
        params = agent.receive_parameters(['latitude', 'longitude'])  # expects string values
        latitude = params.get('latitude', '').strip()
        longitude = params.get('longitude', '').strip()
        
        # Validate presence and type of latitude/longitude
        if not latitude or not longitude:
            agent.send_output(
                agent_output_name='error',
                agent_result='Missing latitude or longitude parameters.'
            )
            return
        try:
            float_lat = float(latitude)
            float_lon = float(longitude)
        except ValueError:
            agent.send_output(
                agent_output_name='error',
                agent_result='Latitude and longitude must be numbers.'
            )
            return
        
        outputs = {}

        # Current weather endpoint
        current_weather_url = (
            'https://api.open-meteo.com/v1/forecast'
            f'?latitude={float_lat}&longitude={float_lon}'
            '&current=temperature_2m,relative_humidity_2m,rain,weather_code'
        )
        try:
            response_current = requests.get(current_weather_url, timeout=10)
            response_current.raise_for_status()
            outputs['current_weather'] = response_current.json()
        except Exception as e:
            outputs['current_weather'] = {'error': f'Current weather fetch failed: {str(e)}'}

        # Hourly forecast endpoint
        hourly_weather_url = (
            'https://api.open-meteo.com/v1/forecast'
            f'?latitude={float_lat}&longitude={float_lon}'
            '&hourly=temperature_2m,precipitation_probability,weather_code'
        )
        try:
            response_hourly = requests.get(hourly_weather_url, timeout=10)
            response_hourly.raise_for_status()
            outputs['hourly_forecast'] = response_hourly.json()
        except Exception as e:
            outputs['hourly_forecast'] = {'error': f'Hourly weather fetch failed: {str(e)}'}

        # Send combined output
        agent.send_output(
            agent_output_name='weather_forecast',
            agent_result=outputs
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result=f'Unexpected agent error: {str(e)}'
        )

def main():
    agent = MofaAgent(agent_name='WeatherForecastNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
