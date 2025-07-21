from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive an auxiliary dummy input for pipeline compatibility
    user_input = agent.receive_parameter('user_input')
    
    try:
        # API endpoint and parameters (from config)
        endpoint = "https://disease.sh/v3/covid-19/historical/all"
        params = {"lastdays": "all"}

        # Make the GET request
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Try to parse as JSON
        try:
            data = response.json()
        except Exception as json_err:
            agent.send_output(
                agent_output_name='covid_trends_error',
                agent_result=f"Error parsing response as JSON: {str(json_err)}"
            )
            return

        # Ensure serialization
        if not isinstance(data, (dict, list, str)):
            agent.send_output(
                agent_output_name='covid_trends_error',
                agent_result="Output is not serializable!"
            )
            return

        # Send successful output
        agent.send_output(
            agent_output_name='covid_trends',
            agent_result=data
        )
    except requests.RequestException as req_err:
        agent.send_output(
            agent_output_name='covid_trends_error',
            agent_result=f"Request error: {str(req_err)}"
        )
    except Exception as err:
        agent.send_output(
            agent_output_name='covid_trends_error',
            agent_result=f"Unhandled error: {str(err)}"
        )

def main():
    agent = MofaAgent(agent_name='Covid19TrendsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# This agent requires 'requests' package. Ensure it is listed in requirements.txt or similar setup documentation.
