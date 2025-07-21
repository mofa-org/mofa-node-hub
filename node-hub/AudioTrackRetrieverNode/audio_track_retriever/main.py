from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate dataflow from other nodes (even if not strictly required)
    user_input = agent.receive_parameter('user_input')  # May remain unused if not needed

    # Define the API endpoint
    api_url = "https://www.theaudiodb.com/api/v1/json/2/search.php"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The AudioDB returns JSON, ensure it's serializable
        tracks_data = response.json()
    except Exception as e:
        # Handle all errors and serialize error message
        error_msg = {'error': True, 'message': str(e)}
        agent.send_output(
            agent_output_name='audio_tracks',
            agent_result=error_msg
        )
        return

    # Deliver the output (can be a dict/list per API)
    agent.send_output(
        agent_output_name='audio_tracks',
        agent_result=tracks_data
    )

def main():
    agent = MofaAgent(agent_name='AudioTrackRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
