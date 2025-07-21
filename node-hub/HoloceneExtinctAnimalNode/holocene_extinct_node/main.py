from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Since this API does not need any input, to facilitate other nodes, we still receive a dummy input
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://extinct-api.herokuapp.com/api/v1/animal/"

    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()  # Assuming the API returns JSON
    except Exception as e:
        # Error containment
        error_message = {'error': str(e)}
        agent.send_output(
            agent_output_name='holocene_extinct_animals',
            agent_result=error_message
        )
        return

    # Valid output via serialization
    agent.send_output(
        agent_output_name='holocene_extinct_animals',
        agent_result=data
    )

def main():
    agent = MofaAgent(agent_name='HoloceneExtinctAnimalNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
