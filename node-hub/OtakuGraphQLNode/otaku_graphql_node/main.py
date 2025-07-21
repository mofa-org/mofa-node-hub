from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependencies: requests
# Make sure to add 'requests' to your requirements.txt or environment setup.

@run_agent
def run(agent: MofaAgent):
    try:
        # Always receive user input to maintain dataflow compatibility
        user_input = agent.receive_parameter('user_input')

        # Required inputs for GraphQL
        graphql_query = agent.receive_parameter('graphql_query')  # String: The GraphQL query string
        variables_str = agent.receive_parameter('variables')      # String: JSON-formatted variables or empty '{}'

        # Type validation and safety
        try:
            variables = json.loads(variables_str) if variables_str else {}
        except Exception as err:
            agent.send_output(
                agent_output_name='graphql_error',
                agent_result=f"Invalid variables JSON: {str(err)}"
            )
            return

        endpoint = "https://api.fussy.fun/graphql"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "query": graphql_query,
            "variables": variables
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
        except Exception as err:
            agent.send_output(
                agent_output_name='graphql_error',
                agent_result=f"Request failed: {str(err)}"
            )
            return

        try:
            api_result = response.json()
        except Exception as err:
            agent.send_output(
                agent_output_name='graphql_error',
                agent_result=f"Response not JSON: {str(err)}"
            )
            return

        agent.send_output(
            agent_output_name='graphql_response',
            agent_result=api_result  # Ensured serializable (dict)
        )
    except Exception as agent_error:
        agent.send_output(
            agent_output_name='graphql_error',
            agent_result=str(agent_error)
        )

def main():
    agent = MofaAgent(agent_name='OtakuGraphQLNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
