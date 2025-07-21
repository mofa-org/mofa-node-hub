# Dependencies:
#   - requests
#   - python-dotenv (if you need to load .env configurations, not required here)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Accept latitude and longitude from dora-rs dataflow as strings
        params = agent.receive_parameters(['latitude', 'longitude'])
        latitude_str = params.get('latitude', '40.6943')  # default value from config.yml
        longitude_str = params.get('longitude', '-73.9249')  # default value from config.yml

        # Type conversion: ensure valid float
        try:
            latitude = float(latitude_str)
            longitude = float(longitude_str)
        except Exception as e:
            agent.send_output(
                agent_output_name='uv_result',
                agent_result={
                    'error': True,
                    'message': f'Invalid coordinates supplied: {e}'
                }
            )
            return

        endpoint = "https://currentuvindex.com/api/v1/uvi"
        payload = {
            'latitude': latitude,
            'longitude': longitude
        }
        try:
            response = requests.get(endpoint, params=payload, timeout=10)
            response.raise_for_status()
            result_data = response.json()
            # Validate serializability (should be dict)
        except Exception as e:
            agent.send_output(
                agent_output_name='uv_result',
                agent_result={
                    'error': True,
                    'message': f'API request failed: {e}'
                }
            )
            return

        agent.send_output(
            agent_output_name='uv_result',
            agent_result=result_data
        )

    except Exception as err:
        agent.send_output(
            agent_output_name='uv_result',
            agent_result={
                'error': True,
                'message': f'Unhandled Agent error: {err}'
            }
        )

def main():
    agent = MofaAgent(agent_name='UVIndexRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
