from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes to call this agent even without input
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = "https://data.tg.ch/api/explore/v2.1/catalog/datasets/sk-stat-56/records"
        params = {"limit": "100"}
        response = requests.get(endpoint, params=params, timeout=30)

        try:
            response.raise_for_status()
        except Exception as http_err:
            agent.send_output(
                agent_output_name='error',
                agent_result={
                    "error": True,
                    "message": f"HTTP error occurred: {str(http_err)}",
                    "status_code": response.status_code
                }
            )
            return

        try:
            json_data = response.json()
        except Exception as json_err:
            agent.send_output(
                agent_output_name='error',
                agent_result={
                    "error": True,
                    "message": f"Failed to parse JSON: {str(json_err)}"
                }
            )
            return

        # All good, deliver the data
        agent.send_output(
            agent_output_name='thurgau_population_data',
            agent_result=json_data if isinstance(json_data, (dict, list)) else str(json_data)
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result={
                "error": True,
                "message": f"An unexpected error occurred: {str(e)}"
            }
        )

def main():
    agent = MofaAgent(agent_name='ThurgauPopulationApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   requests
#   mofa.agent_build.base.base_agent (provided by framework)
#
# Notes:
#   - All output is serializable
#   - Inputs/outputs are handled via framework
#   - Usage: add this agent to your dataflow, trigger via 'user_input' even if none is required