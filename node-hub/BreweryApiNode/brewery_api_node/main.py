from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive 'endpoint_type' to determine which OpenBreweryDB endpoint to use ('list' or 'single')
        endpoint_type = agent.receive_parameter('endpoint_type')  # expects: 'list' or 'single'

        # If 'single', require 'brewery_id'
        params = {}
        if endpoint_type == 'single':
            brewery_id = agent.receive_parameter('brewery_id')
            endpoint = f"https://api.openbrewerydb.org/v1/breweries/{brewery_id}"
        elif endpoint_type == 'list':
            endpoint = "https://api.openbrewerydb.org/v1/breweries"
        else:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={"error": "Invalid endpoint_type. Use 'list' or 'single'."}
            )
            return

        response = requests.get(endpoint)
        if response.status_code == 200:
            # Output must be serializable (list for list, dict for single)
            try:
                data = response.json()
            except Exception as e2:
                data = {"error": f"Failed to parse response: {str(e2)}"}
        else:
            data = {"error": f"Request failed: {response.status_code}"}

        agent.send_output(
            agent_output_name='api_response',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BreweryApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
