from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# requests

@run_agent
def run(agent: MofaAgent):
    """
    Stateless Agent that fetches a random Tronald Dump quote from the official API.
    Documentation: https://docs.tronalddump.io/?ref=freepublicapis.com
    Output is always a dict with the received quote and attribution information.
    """
    # Facilitate calling by adding universal input reception
    user_input = agent.receive_parameter('user_input')

    try:
        response = requests.get('https://api.tronalddump.io/random/quote', timeout=10)
        response.raise_for_status()
        data = response.json()
        # Extract essential info, ensure all fields are serializable
        result = {
            'quote': data.get('value', ''),
            'source': data.get('_embedded', {}).get('source', [{}])[0].get('url', None),
            'appearances': data.get('appearances', None),
            'created_at': data.get('created_at', None),
            'tags': data.get('tags', []),
        }
        agent.send_output(
            agent_output_name='tronald_dump_quote',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='tronald_dump_quote',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='TronaldDumpQuoteNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
