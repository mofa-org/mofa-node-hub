from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Add placeholder input to facilitate framework calls, though APIs require no input
    user_input = agent.receive_parameter('user_input')

    results = {}
    try:
        # Query https://api.dawum.de/newest_surveys.json
        response_newest = requests.get('https://api.dawum.de/newest_surveys.json', timeout=10)
        response_newest.raise_for_status()
        results['newest_surveys'] = response_newest.json()
    except Exception as err:
        results['newest_surveys'] = {'error': str(err)}

    try:
        # Query https://api.dawum.de/
        response_main = requests.get('https://api.dawum.de/', timeout=10)
        response_main.raise_for_status()
        results['main_page'] = response_main.text  # Root endpoint returns HTML, not JSON
    except Exception as err:
        results['main_page'] = {'error': str(err)}

    # Output results (dict is serializable if only strings/dicts/lists inside)
    agent.send_output(
        agent_output_name='german_election_api_results',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='GermanElectionSurveyNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
