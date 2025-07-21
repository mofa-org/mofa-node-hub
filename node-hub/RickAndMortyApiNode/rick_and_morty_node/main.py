# Dependencies: requests (install via pip if necessary)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No required input parameters as per the API specification
    user_input = agent.receive_parameter('user_input')  # For dataflow compatibility
    
    base_url = "https://rickandmortyapi.com/api/"
    endpoints = {
        'episodes': 'episode',
        'characters': 'character',
        'locations': 'location',
    }
    api_results = {}

    for key, path in endpoints.items():
        try:
            response = requests.get(base_url + path, timeout=10)
            response.raise_for_status()
            api_results[key] = response.json()
        except requests.RequestException as e:
            api_results[key] = {'error': str(e)}
        except Exception as e:
            api_results[key] = {'error': 'Unexpected error: ' + str(e)}

    # Output should be serializable (dict)
    agent.send_output(
        agent_output_name='rickandmorty_full_data',
        agent_result=api_results
    )

def main():
    agent = MofaAgent(agent_name='RickAndMortyApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
