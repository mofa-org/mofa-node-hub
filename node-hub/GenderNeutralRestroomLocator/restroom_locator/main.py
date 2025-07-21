from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Even if no inputs, ensure flow compatibility:
        user_input = agent.receive_parameter('user_input')

        endpoint = "https://www.refugerestrooms.org/api/v1/restrooms/"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Ensure data can be serialized
        restrooms = response.json()
        agent.send_output(
            agent_output_name='restroom_data',
            agent_result=restrooms if isinstance(restrooms, (dict, list)) else str(restrooms)
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='restroom_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='GenderNeutralRestroomLocator')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests