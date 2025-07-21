from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        input_mode = agent.receive_parameter('input_mode')  # 'single' or 'multiple'
        if input_mode not in ['single', 'multiple']:
            raise ValueError(f"Invalid input_mode: {input_mode}. Must be 'single' or 'multiple'.")

        if input_mode == 'single':
            latitude = agent.receive_parameter('latitude')
            longitude = agent.receive_parameter('longitude')
            # Validate and convert
            lat = float(latitude)
            lon = float(longitude)
            endpoint = f"https://www.elevation-api.eu/v1/elevation/{lat}/{lon}?json"
        else:  # 'multiple'
            pts = agent.receive_parameter('pts')   # expects a string like "[[lat1,lon1],[lat2,lon2]]"
            # _Note_: pts must be a string representation of a list of [lat, lon] pairs
            endpoint = f"https://www.elevation-api.eu/v1/elevation?pts={pts}"
        
        # Make the GET request
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        try:
            result = response.json()
        except Exception:
            result = response.text  # Fallback if not JSON
        agent.send_output(
            agent_output_name='elevation_result',
            agent_result=result if isinstance(result, (dict, list)) else str(result)
        )
    except Exception as err:
        agent.send_output(
            agent_output_name='elevation_result',
            agent_result={'error': str(err)}
        )

def main():
    agent = MofaAgent(agent_name='ElevationApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
