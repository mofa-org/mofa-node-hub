from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
from typing import Any, Dict

# Dependencies:
# - requests
# Ensure this dependency is specified in requirements.yml if not already present.

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # Enables compatibility with orchestrators, even when unused

    endpoint = "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100088/records"
    params = {
        'limit': '20'
    }
    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure the output is serializable (dict)
        agent.send_output(
            agent_output_name='parking_data',
            agent_result=data
        )
    except Exception as e:
        # Return the error as a string for serialization compliance
        agent.send_output(
            agent_output_name='parking_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BaselParkingDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
