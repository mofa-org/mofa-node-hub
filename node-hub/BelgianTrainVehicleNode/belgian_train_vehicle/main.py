from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate graph linking, accept a dummy input parameter (not used)
    user_input = agent.receive_parameter('user_input')

    # Define API endpoint and parameters
    endpoint = "https://api.irail.be/v1/vehicle/"
    params = {
        'id': 'BE.NMBS.IC1832',
        'format': 'json',
        'lang': 'en',
        'alerts': 'false'
    }
    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        # The response is expected to be JSON serializable
        result = response.json()
        agent.send_output(
            agent_output_name='vehicle_data',
            agent_result=result
        )
    except Exception as e:
        # Output the error message in a serializable format
        agent.send_output(
            agent_output_name='vehicle_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BelgianTrainVehicleNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# To install: pip install requests
