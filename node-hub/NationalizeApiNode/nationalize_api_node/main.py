from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Input Handling: receive 'name' parameter as string
    try:
        name = agent.receive_parameter('name')
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Input parameter "name" must be a non-empty string.')

        # API Call to Nationalize.io
        api_url = 'https://api.nationalize.io/'
        params = {'name': name}
        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()  # Will raise HTTPError for bad response
        result = response.json()
        # Serialization validation
        if not isinstance(result, dict):
            raise ValueError('API response is not a dictionary.')
    except Exception as e:
        # Contain all errors, output as error message
        result = {'error': True, 'message': str(e)}

    agent.send_output(
        agent_output_name='nationalize_result',
        agent_result=result # Always a serializable type (dict)
    )

def main():
    agent = MofaAgent(agent_name='NationalizeApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
