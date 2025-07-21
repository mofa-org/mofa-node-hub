# Dependencies: requests
# Ensure the `requests` package is present in your environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No required business input, but receive a placeholder for dataflow compatibility
    user_input = agent.receive_parameter('user_input')  # For dataflow connectivity, not used
    output = {}
    endpoints = {
        'characters': 'https://api.attackontitanapi.com/characters',
        'episodes': 'https://api.attackontitanapi.com/episodes',
        'organizations': 'https://api.attackontitanapi.com/organizations',
        'locations': 'https://api.attackontitanapi.com/locations',
        'titans': 'https://api.attackontitanapi.com/titans',
        'routes': 'https://api.attackontitanapi.com',
    }
    for key, url in endpoints.items():
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            try:
                data = response.json()
            except Exception:
                data = response.text
            output[key] = data
        except Exception as e:
            output[key] = {'error': str(e)}
    agent.send_output(
        agent_output_name='aot_api_data',
        agent_result=output
    )

def main():
    agent = MofaAgent(agent_name='AttackOnTitanApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
