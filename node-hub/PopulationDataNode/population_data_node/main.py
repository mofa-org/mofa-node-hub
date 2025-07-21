# population_data_node/agent.py
# Dependencies: requests (install via pip if missing)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # For compatibility with calling nodes
    try:
        endpoint = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            error_msg = f"Failed to decode JSON: {str(e)}"
            agent.send_output(
                agent_output_name='population_api_error',
                agent_result={'error': error_msg}
            )
            return
        agent.send_output(
            agent_output_name='population_data',
            agent_result=data
        )
    except requests.RequestException as req_err:
        agent.send_output(
            agent_output_name='population_api_error',
            agent_result={'error': str(req_err)}
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='population_api_error',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='PopulationDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
