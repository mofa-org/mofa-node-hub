# Dependencies:
#   requests (public HTTP client)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Dora-rs compliant agent to fetch film camera data from https://filmapi.vercel.app/api/films.
    No input required, but to facilitate graph integration, a dummy parameter is received for compatibility.
    """
    # Facilitate data flow integration even if no real input
    user_input = agent.receive_parameter('user_input')  # Passed-through or ignored

    api_url = "https://filmapi.vercel.app/api/films"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # Film API returns JSON data
        film_data = response.json()
        if not isinstance(film_data, (dict, list)):
            raise ValueError("Non-serializable API response.")
    except Exception as e:
        # Contain errors within agent scope
        agent.send_output(
            agent_output_name='film_api_error',
            agent_result={"error": str(e)}
        )
        return

    # Successful fetch -- deliver data
    agent.send_output(
        agent_output_name='film_api_output',
        agent_result=film_data  # Already serializable (dict/list)
    )

def main():
    agent = MofaAgent(agent_name='FilmDataApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
