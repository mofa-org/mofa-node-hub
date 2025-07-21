from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input: receive Facebook video URL as string
        video_url = agent.receive_parameter('url')
        if not isinstance(video_url, str) or not video_url.strip():
            agent.send_output(
                agent_output_name='error',
                agent_result="Invalid or empty URL. Please provide a Facebook video URL as input."
            )
            return

        # Prepare endpoint
        api_endpoint = "https://fdown.hideme.eu.org/?url=" + video_url
        
        # Send GET request to the API endpoint
        response = requests.get(api_endpoint, timeout=15)
        if response.status_code != 200:
            agent.send_output(
                agent_output_name='error',
                agent_result=f"API responded with status code: {response.status_code}"
            )
            return

        # Try to parse the response as JSON, fallback to text
        try:
            api_result = response.json()
        except Exception:
            api_result = response.text  # fallback if not JSON

        # Output
        agent.send_output(
            agent_output_name='video_download_info',
            agent_result=api_result
        )

    except Exception as e:
        # Error containment
        agent.send_output(
            agent_output_name='error',
            agent_result=str(e)
        )

def main():
    agent = MofaAgent(agent_name='FacebookVideoDownloaderNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests
  Install with: pip install requests
'''
