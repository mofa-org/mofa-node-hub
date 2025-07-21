# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Dummy input to facilitate orchestration
    user_input = agent.receive_parameter('user_input')

    try:
        # API 1: Fetch wonder categories
        cat_resp = requests.get("https://www.world-wonders-api.org/v0/wonders/categories", timeout=10)
        cat_resp.raise_for_status()
        categories = cat_resp.json()
    except Exception as e:
        agent.send_output('categories', {'error': f'Failed to fetch categories: {str(e)}'})
        categories = None

    try:
        # API 2: Fetch all wonders
        wonders_resp = requests.get("https://www.world-wonders-api.org/v0/wonders/", timeout=10)
        wonders_resp.raise_for_status()
        wonders = wonders_resp.json()
    except Exception as e:
        agent.send_output('wonders', {'error': f'Failed to fetch wonders: {str(e)}'})
        wonders = None

    # Output serializable results to respective ports
    if categories is not None:
        agent.send_output('categories', categories)
    if wonders is not None:
        agent.send_output('wonders', wonders)

def main():
    agent = MofaAgent(agent_name='WorldWondersNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
