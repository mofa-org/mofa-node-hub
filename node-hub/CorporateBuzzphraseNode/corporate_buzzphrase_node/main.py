from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes, even though this API needs no input
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://corporatebs-generator.sameerkumar.website/', timeout=10)
        response.raise_for_status()
        data = response.json()
        # The API returns JSON with a 'phrase' key
        phrase = data.get('phrase', "")
        # Ensure output is serialized string
        agent.send_output(
            agent_output_name='buzzphrase',
            agent_result=str(phrase)
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='buzzphrase',
            agent_result=str(f"Error: {e}")
        )

def main():
    agent = MofaAgent(agent_name='CorporateBuzzphraseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Dataflow Ports:
- Input: 'user_input' (for compatibility; ignored)
- Output: 'buzzphrase' (returns the generated corporate BS phrase or error message)
"""