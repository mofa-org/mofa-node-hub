from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# Dependencies: requests
# Configuration: deck_id, deck_count, draw_count can be set in the config
def get_config_param(name, default=None):
    # Try env first
    return os.getenv(name.upper(), default)

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate input from upstream if any (mandatory - see instructions)
        user_input = agent.receive_parameter('user_input')

        # Configurations - default values as per config/yml
        base_url = "https://www.deckofcardsapi.com/api"
        deck_id = get_config_param('deck_id', '1xou3n64udg9')
        deck_count = int(get_config_param('deck_count', 1))
        draw_count = int(get_config_param('draw_count', 2))

        # Action Routing: user_input string can indicate action ('shuffle', 'new_deck', 'draw')
        action = 'shuffle'  # default action
        param = None
        if user_input:
            user_input = user_input.strip().lower()
            if 'new' in user_input:
                action = 'new_deck'
            elif 'draw' in user_input:
                action = 'draw'
            elif 'shuffle' in user_input:
                action = 'shuffle'

        result = {}
        if action == 'shuffle':
            endpoint = f"{base_url}/{deck_id}/shuffle/"
            resp = requests.get(endpoint)
            result = resp.json()
            if resp.status_code != 200:
                raise RuntimeError(f"Shuffle failed: {result}")
        elif action == 'new_deck':
            endpoint = f"{base_url}/deck/new/shuffle/?deck_count={deck_count}"
            resp = requests.get(endpoint)
            result = resp.json()
            if resp.status_code != 200:
                raise RuntimeError(f"New deck creation failed: {result}")
        elif action == 'draw':
            endpoint = f"{base_url}/{deck_id}/draw/?count={draw_count}"
            resp = requests.get(endpoint)
            result = resp.json()
            if resp.status_code != 200:
                raise RuntimeError(f"Draw failed: {result}")
        else:
            result = {'error': f'Unknown action: {action}'}

        # Ensure serializability
        agent.send_output(
            agent_output_name='deck_api_response',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='deck_api_response',
            agent_result={
                'error': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='DeckOfCardsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
