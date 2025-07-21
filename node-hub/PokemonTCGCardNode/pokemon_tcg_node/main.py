from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Input for integration, to help other nodes chain to this node if needed
    user_input = agent.receive_parameter('user_input')

    api_endpoint = "https://api.pokemontcg.io/v2/cards"
    try:
        response = requests.get(api_endpoint, timeout=10)
        response.raise_for_status()
        # Try to get JSON, contain any parse issues
        data = response.json()
        # To ensure serialization, send a dictionary (potentially truncated for safety)
        # If response is too large, maybe return the first few cards only
        cards = data.get('data', [])
        output = {'cards_preview': cards[:10]} if isinstance(cards, list) else {'cards_preview': cards}
        agent.send_output(
            agent_output_name='pokemon_tcg_cards',
            agent_result=output
        )
    except Exception as e:
        # Catch and return error
        agent.send_output(
            agent_output_name='pokemon_tcg_cards',
            agent_result={
                'error': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='PokemonTCGCardNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
