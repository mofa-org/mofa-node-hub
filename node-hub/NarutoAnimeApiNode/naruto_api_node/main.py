from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Fetch all villages, teams, and characters from the Naruto anime API, and output the results as a dictionary.
    """
    # To stay stateless and allow other nodes to trigger the run,
    # facilitate input compatibility, even though this agent needs no true input:
    user_input = agent.receive_parameter('user_input')  # for workflow chaining

    endpoints = {
        'villages': 'https://narutodb.xyz/api/village',
        'teams': 'https://narutodb.xyz/api/team',
        'characters': 'https://narutodb.xyz/api/character',
    }

    results = {}
    errors = {}
    for key, url in endpoints.items():
        try:
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            results[key] = data
        except Exception as e:
            results[key] = None
            errors[key] = f"Error: {str(e)}"

    # Output results under agent_output_name 'naruto_api_outputs'
    output_payload = {
        'results': results,
        'errors': errors
    }
    agent.send_output(
        agent_output_name='naruto_api_outputs',
        agent_result=output_payload
    )

def main():
    agent = MofaAgent(agent_name='NarutoAnimeApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
# Dependencies:
# - requests (install via `pip install requests`)
"""