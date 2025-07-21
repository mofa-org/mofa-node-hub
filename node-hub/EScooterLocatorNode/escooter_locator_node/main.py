from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    """
    dora-rs agent: EScooterLocatorNode
    Description: Get all available E-Scooters within 500m of a specific point using Swiss Shared Mobility API.
    Inputs:
        - lat (str): Latitude as a string.
        - lon (str): Longitude as a string.
    Outputs:
        - escooter_results (dict or str): Serializable API response or error.
    Required dependencies:
        - requests
    Documentation: https://github.com/SFOE/sharedmobility/blob/main/Sharedmobility.ch-API.md?ref=freepublicapis.com
    """
    try:
        # Accept user input for compatibility with other nodes (even if not used directly)
        user_input = agent.receive_parameter('user_input')

        # Receive latitude and longitude as strings
        params = agent.receive_parameters(['lat', 'lon'])
        lat = params.get('lat')
        lon = params.get('lon')

        # Validate and convert input types
        try:
            lat_f = float(lat)
            lon_f = float(lon)
        except (TypeError, ValueError):
            agent.send_output(
                agent_output_name='escooter_results',
                agent_result={'error': 'Invalid latitude or longitude; must be convertible to float.'}
            )
            return

        # Endpoint and default parameters
        endpoint = "https://api.sharedmobility.ch/v1/sharedmobility/identify"
        default_params = {
            'filters': 'ch.bfe.sharedmobility.vehicle_type=E-Scooter',
            'Geometry': f"{lon_f},{lat_f}",
            'Tolerance': 500,
            'offset': 0,
            'geometryFormat': 'esrijson',
        }

        try:
            response = requests.get(endpoint, params=default_params, timeout=10)
            response.raise_for_status()
            api_result = response.json()
            # Validate serialization
            try:
                import json
                json.dumps(api_result)
            except Exception:
                api_result = str(api_result)
        except Exception as e:
            api_result = {'error': f'API request failed: {str(e)}'}

        agent.send_output(
            agent_output_name='escooter_results',
            agent_result=api_result
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='escooter_results',
            agent_result={'error': f'Unhandled exception: {str(ex)}'}
        )

def main():
    agent = MofaAgent(agent_name='EScooterLocatorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
