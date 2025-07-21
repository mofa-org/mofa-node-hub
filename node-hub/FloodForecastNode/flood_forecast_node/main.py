from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    FloodForecastNode fetches simulated river discharge data from Open-Meteo Flood API.

    Expects input parameters:
      - latitude (string representing float)
      - longitude (string representing float)
      - daily (string, e.g., 'river_discharge')

    Returns output on 'flood_forecast' port as JSON-serializable dict.
    """
    try:
        # Receive input parameters (all as strings)
        params = agent.receive_parameters(['latitude', 'longitude', 'daily'])
        
        # Type conversion and defaulting
        latitude = float(params.get('latitude', '59.91'))
        longitude = float(params.get('longitude', '10.75'))
        daily = params.get('daily', 'river_discharge')

        endpoint = "https://flood-api.open-meteo.com/v1/flood"
        query_params = {
            'latitude': latitude,
            'longitude': longitude,
            'daily': daily
        }
        timeout_seconds = 30
        response = requests.get(endpoint, params=query_params, timeout=timeout_seconds)
        response.raise_for_status()
        data = response.json()

        # Output (ensure JSON serializable)
        agent.send_output(
            agent_output_name='flood_forecast',
            agent_result=data
        )
    except Exception as e:
        # Error handling: send error message
        agent.send_output(
            agent_output_name='flood_forecast',
            agent_result={
                'error': True,
                'details': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='FloodForecastNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
