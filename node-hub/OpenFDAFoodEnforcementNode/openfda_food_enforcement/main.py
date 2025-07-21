# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent to fetch the latest 10 food enforcement reports from openFDA.
    No input required for this node, but to ensure compatibility, we receive a dummy parameter.
    Output is sent to 'food_enforcement_data'.
    """
    # No real input required, but to maintain callability:
    user_input = agent.receive_parameter('user_input')
    api_url = "https://api.fda.gov/food/enforcement.json?limit=10"
    try:
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()
        data = response.json()
        # Ensure the output is serializable (dict)
        agent.send_output(
            agent_output_name='food_enforcement_data',
            agent_result=data
        )
    except Exception as e:
        error_message = {'error': str(e)}
        agent.send_output(
            agent_output_name='food_enforcement_data',
            agent_result=error_message
        )

def main():
    agent = MofaAgent(agent_name='OpenFDAFoodEnforcementNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
