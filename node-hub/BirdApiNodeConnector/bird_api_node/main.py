from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate dataflow even if not used
        user_input = agent.receive_parameter('user_input')

        # Accept input parameters for flexibility
        search_param = agent.receive_parameter('search')  # user sends "bald" etc., or empty for all birds
        base_url = "https://freetestapi.com/api/v1/birds"
        headers = {'Accept': 'application/json'}

        # Prepare API request
        if search_param and search_param.strip():
            url = f"{base_url}?search={search_param.strip()}"
        else:
            url = base_url

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        birds_data = response.json()

        # Ensure output is serializable
        agent.send_output(
            agent_output_name='birds_result',
            agent_result=birds_data
        )

    except Exception as e:
        agent.send_output(
            agent_output_name='birds_result',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BirdApiNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
