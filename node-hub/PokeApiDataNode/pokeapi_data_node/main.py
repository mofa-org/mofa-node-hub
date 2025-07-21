# Dependencies: requests (install via pip if needed)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate calls from other nodes, simulate an input parameter even though not required
    user_input = agent.receive_parameter('user_input')
    
    # Define endpoints as per instructions
    endpoints = {
        'species': 'https://pokeapi.co/api/v2/pokemon-species/aegislash',
        'abilities': 'https://pokeapi.co/api/v2/ability/battle-armor',
        'info': 'https://pokeapi.co/api/v2/pokemon/ditto',
    }

    results = {}
    for key, url in endpoints.items():
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            results[key] = data
        except Exception as e:
            # Contain error and serialize message
            results[key] = {'error': str(e)}
    
    # Send results via output port
    agent.send_output(
        agent_output_name='pokeapi_data',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='PokeApiDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()