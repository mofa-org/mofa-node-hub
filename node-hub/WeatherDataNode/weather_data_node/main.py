from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # To facilitate other nodes to call
        user_input = agent.receive_parameter('user_input')

        # Receive input location as parameter (assume location is city name or similar string)
        location = agent.receive_parameter('location')  # expecting string (city name, etc.)

        # API Key from environment variable (set via .env.secret)
        api_key = os.environ.get('OPENWEATHER_API_KEY')
        if not api_key:
            raise ValueError("OPENWEATHER_API_KEY is not set in environment variables.")
        
        # Prepare request parameters
        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric',  # can be changed or parameterized
        }

        # Make API request
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params=params,
            timeout=10
        )
        
        # Check HTTP status
        if response.status_code != 200:
            try:
                error_detail = response.json()
            except Exception:
                error_detail = response.text
            raise RuntimeError(f"OpenWeatherMap API error {response.status_code}: {error_detail}")

        # Parse response (return JSON serializable dict)
        weather_data = response.json()

        # Output must be serializable (dict)
        agent.send_output(
            agent_output_name='weather_data',
            agent_result=weather_data
        )
    except Exception as e:
        # Graceful error handling
        agent.send_output(
            agent_output_name='weather_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='WeatherDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests (pip install requests)
- Environment: OPENWEATHER_API_KEY must be set in .env.secret
Inputs:
- location (string): Name of the location/city
- user_input: dummy input to facilitate flow
Outputs:
- weather_data (dict): Weather information or error message
"""
