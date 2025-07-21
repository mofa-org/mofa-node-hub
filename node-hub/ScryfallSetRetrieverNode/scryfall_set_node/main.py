# Dependencies: requests
# Ensure `requests` is installed in your environment: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    dora-rs compliant Agent to retrieve Scryfall Aether Revolt set metadata.
    API Doc: https://scryfall.com/docs/api?ref=freepublicapis.com
    No input required; presence of 'user_input' parameter is only for dataflow linkage.
    """
    # Facilitate dataflow linkage for Dora-rs, even though unused
    user_input = agent.receive_parameter('user_input')

    SCRYFALL_SET_ENDPOINT = "https://api.scryfall.com/sets/aer"
    set_data = None
    error = None

    try:
        response = requests.get(SCRYFALL_SET_ENDPOINT, timeout=10)
        response.raise_for_status()
        # Validate response JSON serialization
        set_data = response.json()
    except Exception as exc:
        error = str(exc)
        set_data = {"error": error}

    # Outputs are always serializable
    agent.send_output(
        agent_output_name='scryfall_set_data',
        agent_result=set_data
    )

def main():
    agent = MofaAgent(agent_name='ScryfallSetRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
