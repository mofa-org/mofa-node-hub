# Dependencies:
#   - requests
#   - python-dotenv (for .env.secret support if needed)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    WeatherApiNodeConnector Agent
    - Receives input: city_name (string via 'city_name' port)
    - Calls GoWeather API endpoint for Curitiba or Bern based on input
    - Outputs weather data (dict) via 'weather_result' port
    - Stateless and fully error contained
    """
    try:
        city_name = agent.receive_parameter('city_name')  # Always a string
        if not city_name:
            raise ValueError('city_name input is required.')
        # Map city names to endpoints
        endpoints = {
            'curitiba': 'https://goweather.herokuapp.com/weather/Curitiba',
            'bern': 'https://goweather.herokuapp.com/weather/bern'
        }
        city_key = city_name.strip().lower()
        if city_key not in endpoints:
            agent.send_output(
                agent_output_name='weather_result',
                agent_result={
                    'error': f"Unsupported city: {city_name}. Try 'Curitiba' or 'Bern'."
                }
            )
            return
        url = endpoints[city_key]
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            # Ensure all values are serializable and strings
            for k,v in data.items():
                if not isinstance(v, str) and v is not None:
                    data[k] = str(v)
            agent.send_output(
                agent_output_name='weather_result',
                agent_result=data
            )
        else:
            agent.send_output(
                agent_output_name='weather_result',
                agent_result={
                    'error': f"Weather API returned status {resp.status_code} for city {city_name}"
                }
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='weather_result',
            agent_result={
                'error': f"Exception occurred: {str(e)}"
            }
        )

def main():
    agent = MofaAgent(agent_name='WeatherApiNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
