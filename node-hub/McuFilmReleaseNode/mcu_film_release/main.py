from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Retrieves information about the next MCU film release from the API
    Endpoint: https://www.whenisthenextmcufilm.com/api (GET)
    Since no input parameter is needed, a dummy receive_parameter call is added for compatibility.
    """
    try:
        # For DAG compatibility – allows other nodes to call this agent as a node
        user_input = agent.receive_parameter('user_input')

        api_url = "https://www.whenisthenextmcufilm.com/api"
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()  # dict - should be serializable
    except Exception as e:
        # Handle all errors and return a str error message
        data = {"error": str(e)}

    agent.send_output(
        agent_output_name='mcu_film_release_info',
        agent_result=data  # dict is serializable
    )

def main():
    agent = MofaAgent(agent_name='McuFilmReleaseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
