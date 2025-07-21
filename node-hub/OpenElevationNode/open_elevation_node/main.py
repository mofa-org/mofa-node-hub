from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling (default to facilitate upstream nodes)
        user_input = agent.receive_parameter('user_input')

        # Receive 'locations' parameter or fallback to default
        params = agent.receive_parameters(['locations'])
        locations = params.get('locations')
        if locations is None or locations.strip() == '':
            # Fallback to default from config (Port safe string)
            locations = "41.161758,-8.583933"

        # Prepare endpoint and request
        endpoint = "https://api.open-elevation.com/api/v1/lookup"
        query_params = {"locations": locations}

        response = requests.get(endpoint, params=query_params, timeout=10)
        response.raise_for_status()

        # Validate and serialize output
        try:
            elevation_data = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='elevation_response',
                agent_result={"error": "Invalid JSON response", "details": str(e)}
            )
            return

        agent.send_output(
            agent_output_name='elevation_response',
            agent_result=elevation_data
        )

    except Exception as e:
        # Error containment and serialization
        agent.send_output(
            agent_output_name='elevation_response',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='OpenElevationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
