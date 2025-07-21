from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input
        param_dict = agent.receive_parameters(['locations', 'interpolation'])
        locations = param_dict.get('locations', '')
        interpolation = param_dict.get('interpolation', 'cubic')
        
        # Input validation
        if not locations:
            agent.send_output(
                agent_output_name='error',
                agent_result='Missing required parameter: locations.'
            )
            return

        # Build API URL
        base_url = "https://api.opentopodata.org/v1/srtm90m"
        params = {
            'locations': locations,
            'interpolation': interpolation
        }
        timeout = 30  # Default timeout (seconds)
                
        # Attempt API call
        response = requests.get(base_url, params=params, timeout=timeout)
        response.raise_for_status()
        data = response.json()

        agent.send_output(
            agent_output_name='elevation_result',
            agent_result=data
        )

    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result=str(e)
        )

def main():
    agent = MofaAgent(agent_name='ElevationCoordinateNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Dataflow Port Definitions:
- Receives: 'locations' (str), 'interpolation' (str, optional)
- Outputs: 'elevation_result' (dict), or 'error' (str)
- Input/output via MofaAgent API only
- Stateless and fully self-contained
"""