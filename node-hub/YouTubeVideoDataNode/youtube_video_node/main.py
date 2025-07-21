from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive the 'search_text' input parameter (string expected)
    try:
        search_text = agent.receive_parameter('search_text')
        if not search_text:
            # Fallback to default value if no input is provided
            search_text = 'heat waves'
    except Exception:
        # Default if error occurs during parameter reception
        search_text = 'heat waves'

    # Endpoint from configuration
    endpoint = "https://abhi-api.vercel.app/api/search/yts"

    # Prepare the request parameters
    params = {'text': search_text}

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        # Ensure the output is serializable
        results = response.json()
    except Exception as e:
        # Handle errors gracefully and return as output
        results = {'error': True, 'message': str(e)}

    # Send the output via the specified dataflow port
    agent.send_output(
        agent_output_name='youtube_video_data',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='YouTubeVideoDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
