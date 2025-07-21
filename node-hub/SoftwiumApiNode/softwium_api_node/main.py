from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this agent if needed
    user_input = agent.receive_parameter('user_input')  # Not used; for dataflow compatibility
    
    api_endpoints = {
        'currencies': 'https://softwium.com/api/currencies',
        'books': 'https://softwium.com/api/books',
        'pokemons': 'https://softwium.com/api/pokemons',
        'peoples': 'https://softwium.com/api/peoples',
    }
    results = {}
    errors = {}
    for key, url in api_endpoints.items():
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            # Safe serialization
            try:
                results[key] = response.json()
            except Exception as json_err:
                results[key] = response.text
                errors[key] = f'JSON decode error: {json_err}'
        except Exception as e:
            results[key] = None
            errors[key] = str(e)
    agent.send_output(
        agent_output_name='softwium_data',
        agent_result={
            'data': results,
            'errors': errors
        }
    )

def main():
    agent = MofaAgent(agent_name='SoftwiumApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()