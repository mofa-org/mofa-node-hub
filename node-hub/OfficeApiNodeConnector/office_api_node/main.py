# Dependencies: requests
# Make sure requests is installed (pip install requests)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

API_ENDPOINTS = {
    'episodes': 'https://theofficeapi.dev/api/episodes',
    'characters': 'https://theofficeapi.dev/api/characters'
}
TIMEOUT = 10  # seconds

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input param specifying which API data to fetch
        api_type = agent.receive_parameter('api_type')  # "episodes" or "characters"
        if not isinstance(api_type, str):
            raise ValueError('api_type input must be a string')

        if api_type not in API_ENDPOINTS:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={
                    'error': f"Invalid api_type: {api_type}. Must be one of: {list(API_ENDPOINTS.keys())}"
                }
            )
            return

        url = API_ENDPOINTS[api_type]
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as json_error:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={
                    'error': 'Failed to parse API response as JSON',
                    'details': str(json_error)
                }
            )
            return

        # Ensure serialization (dict is serializable)
        agent.send_output(
            agent_output_name='api_response',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': 'Internal error occurred',
                'details': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='OfficeApiNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
