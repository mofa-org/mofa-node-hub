from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# Required dependencies:
# - requests
# Ensure you add 'requests' to your requirements.txt or dependency management file.

MAGAZINE_API_BASE_URL = "https://www.freepublicapis.com/magazine-api"
REQUEST_TIMEOUT = 30  # seconds

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive parameters as strings (all inputs are string per mofa interface)
        params = agent.receive_parameters(['categories', 'tags', 'publication_dates'])

        # Prepare params dict for API
        api_params = {}
        for key, value in params.items():
            if value and value != '':
                # The API probably expects comma-separated lists for categories/tags, use as-is
                api_params[key] = value

        # Request the Magazine API
        response = requests.get(
            MAGAZINE_API_BASE_URL,
            params=api_params,
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()  # Raises HTTPError if not 2xx
        result = response.json()

        # Serialization check
        if not isinstance(result, (dict, list)):
            result = str(result)

        agent.send_output(
            agent_output_name='magazine_content_data',
            agent_result=result
        )
    except Exception as e:
        # Contain error and report as output
        error_msg = {'error': str(e)}
        agent.send_output(
            agent_output_name='magazine_content_data',
            agent_result=error_msg
        )

def main():
    agent = MofaAgent(agent_name='MagazineContentConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
