# Dependencies: requests
# Make sure the 'requests' package is available in your environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive input to select endpoint (no user input needed, facilitate chaining)
    user_input = agent.receive_parameter('user_input')  # For compatibility with chaining/other nodes
    try:
        api_endpoints = [
            {
                'endpoint': "https://api.datamuse.com/words?ml=ringing+in+the+ears",
                'description': "words with a meaning similar to ringing in the ears",
            },
            {
                'endpoint': "https://api.datamuse.com/words?sl=jirraf",
                'description': "words that sound like jirraf",
            },
            {
                'endpoint': "https://api.datamuse.com/words?ml=duck&sp=b*",
                'description': "words related to duck that start with the letter b",
            }
        ]
        # Example default: run all three endpoints and return results as dictionary
        results = {}
        for idx, spec in enumerate(api_endpoints):
            try:
                resp = requests.get(spec['endpoint'], timeout=8)
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                data = {'error': str(e)}
            results[spec['description']] = data
        agent.send_output(
            agent_output_name='datamuse_outputs',
            agent_result=results  # dict is serializable and compliant
        )
    except Exception as e:
        # Complete error containment
        agent.send_output(
            agent_output_name='datamuse_outputs',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='DatamuseWordApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
