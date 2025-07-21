# Dependencies: requests
# Ensure to add 'requests' in your requirements.txt or environment setup

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Expect an input command that determines the action. This enables integration with other nodes.
    # Format: action (random_cocktail | ingredient_search | drink_search), param (optional)
    inputs = agent.receive_parameters(['action', 'param'])
    action = inputs.get('action', '').strip().lower()
    param = inputs.get('param', '').strip()

    result = None
    try:
        if action == 'random_cocktail':
            url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            result = resp.json()
        elif action == 'ingredient_search':
            if not param:
                raise ValueError('Missing ingredient name for search.')
            url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?i={param}'
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            result = resp.json()
        elif action == 'drink_search':
            if not param:
                raise ValueError('Missing drink name for search.')
            url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={param}'
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            result = resp.json()
        else:
            result = {'error': f'Unknown action: {action}'}
    except Exception as e:
        result = {'error': str(e)}

    # Ensure output is serializable
    agent.send_output(
        agent_output_name='lookup_result',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='CocktailLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
