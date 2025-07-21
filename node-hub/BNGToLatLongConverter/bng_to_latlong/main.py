from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling
        user_input = agent.receive_parameter('user_input') # Added for chaining compatibility
        east = agent.receive_parameter('easting')
        north = agent.receive_parameter('northing')
        try:
            # Type conversion
            east = str(int(float(east.strip())))
            north = str(int(float(north.strip())))
        except Exception:
            agent.send_output(
                agent_output_name='latlong_result',
                agent_result={
                    'error': 'Easting and Northing must be convertible to integers.'
                }
            )
            return

        # API call
        endpoint = f"https://api.getthedata.com/bng2latlong/{east}/{north}"
        try:
            resp = requests.get(endpoint, timeout=30)
            resp.raise_for_status()
            api_result = resp.json()
        except requests.RequestException as e:
            agent.send_output(
                agent_output_name='latlong_result',
                agent_result={'error': f'API request failed: {str(e)}'}
            )
            return
        except ValueError:
            agent.send_output(
                agent_output_name='latlong_result',
                agent_result={'error': 'Failed to parse API response as JSON.'}
            )
            return

        # Output delivery - enforce serialization
        if isinstance(api_result, dict):
            agent.send_output(
                agent_output_name='latlong_result',
                agent_result=api_result
            )
        else:
            agent.send_output(
                agent_output_name='latlong_result',
                agent_result={'error': 'API response is not a dictionary.'}
            )
    except Exception as general_error:
        agent.send_output(
            agent_output_name='latlong_result',
            agent_result={'error': f'Unexpected error: {str(general_error)}'}
        )

def main():
    agent = MofaAgent(agent_name='BNGToLatLongConverter')
    run(agent=agent)

if __name__ == '__main__':
    main()
