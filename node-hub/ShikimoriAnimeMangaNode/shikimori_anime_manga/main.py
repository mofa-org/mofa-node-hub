# Dependencies: requests
# Ensure that 'requests' is installed in your requirements.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    MOFA Agent for interacting with Shikimori API (Anime & Manga search endpoints).
    - /animes: Fetches a list of anime.
    - /mangas: Fetches a list of manga.
    Accepts one required input: 'content_type' (must be 'anime' or 'manga').
    """
    try:
        # Accepts 'content_type' parameter: should be 'anime' or 'manga'
        content_type = agent.receive_parameter('content_type').strip().lower()

        api_base_url = 'https://shikimori.one/api'
        endpoint_map = {
            'anime': '/animes',
            'manga': '/mangas',
        }
        if content_type not in endpoint_map:
            agent.send_output(
                agent_output_name='error',
                agent_result=f"Invalid content_type '{{content_type}}'. Use 'anime' or 'manga'."
            )
            return

        url = api_base_url + endpoint_map[content_type]
        timeout = 30  # Seconds, per config
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            # Validate serializable output
            result = response.json()
            if not isinstance(result, (dict, list)):
                result = str(result)
            agent.send_output(
                agent_output_name='shikimori_result',
                agent_result=result
            )
        except requests.RequestException as e:
            agent.send_output(
                agent_output_name='error',
                agent_result=f"Request failed: {str(e)}"
            )
    except Exception as e:
        # Full error containment
        agent.send_output(
            agent_output_name='error',
            agent_result=f"Error in ShikimoriAnimeMangaNode: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='ShikimoriAnimeMangaNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
