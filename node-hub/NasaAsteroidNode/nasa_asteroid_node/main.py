from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
from typing import Dict, Any

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive service selection parameter from dataflow
        service_type = agent.receive_parameter('service_type')
        # For compatibility, always receive 'user_input' so downstream nodes can call without error
        user_input = agent.receive_parameter('user_input')
        
        # Load the NASA API key from environment variables (.env.secret)
        NASA_API_KEY = os.getenv('NASA_API_KEY')
        if not NASA_API_KEY:
            agent.send_output(
                agent_output_name='error',
                agent_result='NASA_API_KEY environment variable not set.'
            )
            return

        base_url = 'https://api.nasa.gov/neo/rest/v1'

        # Handle which endpoint to call based on 'service_type'
        if service_type == 'feed':
            # Get additional parameters (date range etc.)
            date_params = agent.receive_parameters(['start_date', 'end_date'])
            # Type conversion and defaults
            start_date = date_params.get('start_date', '2023-09-07')
            end_date = date_params.get('end_date', '2023-09-08')

            endpoint = f"{base_url}/feed"
            params = {
                'start_date': str(start_date),
                'end_date': str(end_date),
                'api_key': NASA_API_KEY
            }
        elif service_type == 'browse':
            endpoint = f"{base_url}/neo/browse"
            params = {
                'api_key': NASA_API_KEY
            }
        else:
            agent.send_output(
                agent_output_name='error',
                agent_result=f"Unsupported service_type: {service_type}"
            )
            return
        # API request
        try:
            response = requests.get(endpoint, params=params, timeout=15)
            response.raise_for_status()
            # Validate serialization: Output must be dict or str
            result_data = response.json()
        except Exception as api_err:
            agent.send_output(
                agent_output_name='error',
                agent_result=str(api_err)
            )
            return
        # Output: agent_output_name follows service_type for clarity
        agent.send_output(
            agent_output_name=f'{service_type}_output',
            agent_result=result_data
        )
    except Exception as err:
        agent.send_output(
            agent_output_name='error',
            agent_result=f"Agent failed: {str(err)}"
        )

def main():
    agent = MofaAgent(agent_name='NasaAsteroidNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
