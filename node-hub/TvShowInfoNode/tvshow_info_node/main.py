# Dependencies: requests
# To install: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    TvShowInfoNode queries TVMaze API for show data and Big Bang Theory images.
    Receives a string parameter 'show_query' (search query for a show).
    Outputs:
        - 'search_results' : Search results for the given `show_query`
        - 'big_bang_images': Images for the show 'Big Bang Theory' (static endpoint)
    """
    try:
        # Receive user search query for show; enforce string
        show_query = agent.receive_parameter('show_query')
        show_query = str(show_query) if show_query is not None else ''  # fallback to empty query

        # TVMaze search endpoint
        search_url = 'https://api.tvmaze.com/search/shows'
        params = {'q': show_query}
        try:
            resp = requests.get(search_url, params=params, timeout=10)
            resp.raise_for_status()
            search_results = resp.json()
        except Exception as e:
            search_results = {'error': f'API error during show search: {str(e)}'}

        # TVMaze images for Big Bang Theory (show id 66)
        images_url = 'https://api.tvmaze.com/shows/66/images'
        try:
            images_resp = requests.get(images_url, timeout=10)
            images_resp.raise_for_status()
            images_result = images_resp.json()
        except Exception as e:
            images_result = {'error': f'API error retrieving Big Bang Theory images: {str(e)}'}

        # Outputs: all outputs must be serializable
        agent.send_output(
            agent_output_name='search_results',
            agent_result=search_results
        )
        agent.send_output(
            agent_output_name='big_bang_images',
            agent_result=images_result
        )
    except Exception as main_e:
        # Top-level error catch (framework compliance, stateless)
        agent.send_output(
            agent_output_name='search_results',
            agent_result={'error': f'Unhandled agent error: {str(main_e)}'}
        )
        agent.send_output(
            agent_output_name='big_bang_images',
            agent_result={'error': f'Unhandled agent error: {str(main_e)}'}
        )

def main():
    agent = MofaAgent(agent_name='TvShowInfoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
