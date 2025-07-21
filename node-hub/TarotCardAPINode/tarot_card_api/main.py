from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# Optional: If using python-dotenv for .env.secret
#from dotenv import load_dotenv
#load_dotenv()

@run_agent
def run(agent: MofaAgent):
    """
    TarotCardAPINode - Retrieves tarot card data from tarotapi.dev, supporting:
        - All cards
        - Random card
        - Court cards
    Input required: 'card_type' (str, one of 'all', 'random', 'courts') via the receive_parameter method.
    Output: Tarot card(s) information as dict (serialized by framework).
    """
    # Input handling
    try:
        card_type = agent.receive_parameter('card_type')  # expects 'all', 'random', or 'courts'
        if not isinstance(card_type, str):
            raise ValueError("Input parameter 'card_type' must be a string.")
    except Exception as e:
        agent.send_output(
            agent_output_name='tarot_card_output',
            agent_result={
                'error': f'Failed to receive parameter: {str(e)}'
            }
        )
        return

    # API config (static as per config)
    BASE_URL = "https://tarotapi.dev/api/v1"
    ENDPOINTS = {
        'all': '/cards',
        'random': '/cards/random',
        'courts': '/cards/courts',
    }
    TIMEOUT = 30
    RETRIES = 3
    USER_AGENT = "TarotCardAPINode/1.0"

    # Map input to endpoints
    endpoint = ENDPOINTS.get(card_type.lower())
    if not endpoint:
        agent.send_output(
            agent_output_name='tarot_card_output',
            agent_result={
                'error': f"Unrecognized card_type '{card_type}'. Use one of: 'all', 'random', 'courts'."
            }
        )
        return

    url = BASE_URL + endpoint

    # API call + error handling
    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})
    last_exc = None
    response_data = None

    for attempt in range(RETRIES):
        try:
            response = session.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            response_data = response.json()
            break  # success
        except Exception as exc:
            last_exc = exc
            continue

    if response_data is not None:
        agent.send_output(
            agent_output_name='tarot_card_output',
            agent_result=response_data
        )
    else:
        agent.send_output(
            agent_output_name='tarot_card_output',
            agent_result={
                'error': f'API request failed after {RETRIES} attempts. Cause: {str(last_exc)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='TarotCardAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()
