from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Standardize input for dataflow node compatibility
        user_input = agent.receive_parameter('user_input')  # For invocation consistency
        artist_name = agent.receive_parameter('artist_name')
        if not artist_name or not artist_name.strip():
            # Fallback to default artist
            artist_name = 'coldplay'

        # Build API request
        endpoint = "https://www.theaudiodb.com/api/v1/json/2/search.php"
        params = {"s": artist_name}
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Serialize/validate output
        agent.send_output(
            agent_output_name='artist_info',
            agent_result=json.dumps(data)  # Serialize result to ensure compliance
        )
    except Exception as e:
        error_msg = f"AudioArtistInfoNode error: {str(e)}"
        agent.send_output(
            agent_output_name='artist_info',
            agent_result=json.dumps({'error': error_msg})
        )

def main():
    agent = MofaAgent(agent_name='AudioArtistInfoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
