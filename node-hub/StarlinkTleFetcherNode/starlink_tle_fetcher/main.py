from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate dataflow integration, accept a dummy user_input parameter even if unused
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://celestrak.org/NORAD/elements/gp.php?INTDES=2020-025&FORMAT=JSON-PRETTY"
    timeout = 30  # seconds (default from config)
    try:
        response = requests.get(endpoint, timeout=timeout)
        response.raise_for_status()
        # Ensure content is JSON serializable, so parse and re-dump if needed
        tle_data = response.json()
        agent.send_output(
            agent_output_name='starlink_tle_output',
            agent_result=tle_data
        )
    except Exception as err:
        # Output error message in a standard, serializable format
        agent.send_output(
            agent_output_name='starlink_tle_output',
            agent_result={
                'error': True,
                'message': str(err)
            }
        )

def main():
    agent = MofaAgent(agent_name='StarlinkTleFetcherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   requests
# Provide in requirements.txt: requests
# Environment: None required, API is public
