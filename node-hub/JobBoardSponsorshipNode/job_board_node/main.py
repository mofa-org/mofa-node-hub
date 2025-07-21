# Dependencies:
# - requests (for HTTP communication)
#
# No input required, but a 'user_input' parameter is received for compatibility with other nodes per requirements.
# Output: 'job_board_data' (dict/list/str)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # For compatibility with dora-rs interface, even though no input is used:
    user_input = agent.receive_parameter('user_input')  # (Not used)
    
    try:
        api_url = "https://arbeitnow.com/api/job-board-api"
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # Arbeitnow API returns JSON data
        try:
            job_board_data = response.json()
        except Exception as e:
            # Fallback: treat as plain text if bad content type
            job_board_data = response.text
    except Exception as err:
        job_board_data = {
            'error': True,
            'message': f"Failed to fetch job board data: {str(err)}"
        }
        # Always guarantee serialization

    # Output on defined dataflow port
    agent.send_output(
        agent_output_name='job_board_data',
        agent_result=job_board_data  # Always dict/list/str
    )

def main():
    agent = MofaAgent(agent_name='JobBoardSponsorshipNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
