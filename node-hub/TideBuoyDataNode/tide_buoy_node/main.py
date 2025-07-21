# Dependencies: requests
# Ensure the 'requests' library is available in your environment. If not, install with: pip install requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate other nodes to call this node by expecting 'user_input', although not used here
        user_input = agent.receive_parameter('user_input')

        # All API endpoints (GET, no input required)
        endpoints = {
            'NOAA_Tide_Predictions': 'https://surftruths.com/api/tide/stations.json',
            'NDBC_Buoy_Data': 'https://surftruths.com/api/buoys.json',
        }

        results = {}
        errors = {}

        for name, url in endpoints.items():
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                # Ensure response is JSON serializable
                results[name] = resp.json()
            except Exception as e:
                errors[name] = str(e)

        output_data = {
            'results': results,
            'errors': errors if errors else None
        }

        agent.send_output(
            agent_output_name='tide_buoy_data',
            agent_result=output_data
        )
    except Exception as outer_err:
        agent.send_output(
            agent_output_name='tide_buoy_data',
            agent_result={'results': {}, 'errors': {'agent': str(outer_err)}}
        )

def main():
    agent = MofaAgent(agent_name='TideBuoyDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
