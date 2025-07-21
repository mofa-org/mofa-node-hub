from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate upstream/downstream connectivity in dataflow
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://getfullyear.com/api/year', timeout=6)
        response.raise_for_status()
        data = response.json()
        # API returns {'year': '2024'} (as a string)
        year = data.get('year', '')
        # Send the year as string or as part of a dictionary for flexibility
        agent.send_output(
            agent_output_name='current_year',
            agent_result={'year': year}
        )
    except Exception as e:
        # Handle all errors and return as part of output for debugging/dataflow integrity
        agent.send_output(
            agent_output_name='current_year',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CurrentYearRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
