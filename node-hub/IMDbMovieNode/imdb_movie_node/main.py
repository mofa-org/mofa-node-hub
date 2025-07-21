# Dependencies:
#   - requests
# 
# python -m pip install requests
#
# This agent supports two operations:
#   1. Get movie details by IMDb tt ID ('tt_id' input)
#   2. Search IMDb movies by keyword ('query' input)
# 
# Input ports:
#   - 'tt_id': IMDb tt ID (e.g., 'tt2250912')
#   - 'query': Search string (e.g., 'Spiderman')
# One of these should be provided at a time. If both are provided, 'tt_id' is prioritized.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        params = agent.receive_parameters(['tt_id', 'query'])
        tt_id = params.get('tt_id')
        query = params.get('query')

        base_url = "https://imdb.iamidiotareyoutoo.com/search"

        # Determine which API call to use
        if tt_id and tt_id.strip():  # Priority: get movie details by tt_id
            endpoint = base_url
            request_params = {'tt': str(tt_id).strip()}
        elif query and query.strip():  # Else, search movies by query
            endpoint = base_url
            request_params = {'q': str(query).strip()}
        else:
            agent.send_output(
                agent_output_name='error',
                agent_result={'error': 'No valid input provided. Provide either tt_id or query.'}
            )
            return

        response = requests.get(endpoint, params=request_params, timeout=8)
        try:
            response.raise_for_status()
        except requests.RequestException as e:
            agent.send_output(
                agent_output_name='error',
                agent_result={'error': f'HTTP request failed: {str(e)}'}
            )
            return

        try:
            data = response.json()  # Ensure JSON serializable
        except Exception:
            agent.send_output(
                agent_output_name='error',
                agent_result={'error': 'Failed to parse JSON from response.'}
            )
            return

        # Output to the correct port
        if 'tt' in request_params:
            output_port = 'movie_details'
        else:
            output_port = 'search_results'
        agent.send_output(
            agent_output_name=output_port,
            agent_result=data
        )

    except Exception as ex:
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': f'Agent internal failure: {str(ex)}'}
        )


def main():
    agent = MofaAgent(agent_name='IMDbMovieNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
