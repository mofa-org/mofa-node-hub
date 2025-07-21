from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Query the Spider-Man IMDB API for information about Spider-Man movies. No input required, but
    to comply with the dora-rs framework, receive an unused parameter for dataflow consistency.
    """
    # This agent takes no actionable input, but to facilitate other nodes, receive user_input parameter
    user_input = agent.receive_parameter('user_input')
    api_endpoint = "https://imdb.iamidiotareyoutoo.com/search?q=Spiderman"
    timeout = 10

    try:
        response = requests.get(api_endpoint, timeout=timeout)
        response.raise_for_status()
        # Ensure output is serializable
        try:
            data = response.json()
        except Exception:
            data = response.text
        agent.send_output(
            agent_output_name='imdb_spiderman_api_response',
            agent_result=data
        )
    except Exception as e:
        err_str = f"IMDBSpiderManApiNode error: {str(e)}"
        agent.send_output(
            agent_output_name='imdb_spiderman_api_response',
            agent_result={"error": err_str}
        )

def main():
    agent = MofaAgent(agent_name='IMDBSpiderManApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
