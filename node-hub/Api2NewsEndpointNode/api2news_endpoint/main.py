# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes to call this, we include a required (but not used) input
    user_input = agent.receive_parameter('user_input')  # Required by interface convention

    api_url = "https://endpoint.api2.news/"
    try:
        # Per API docs, we do a simple GET to the endpoint for the latest news
        response = requests.get(api_url)
        response.raise_for_status()
        # Attempt to decode as JSON, fallback to raw text
        try:
            data = response.json()
        except Exception:
            data = response.text

        agent.send_output(
            agent_output_name='news_articles',
            agent_result=data
        )
    except Exception as e:
        # Error must be handled internally
        agent.send_output(
            agent_output_name='news_articles',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='Api2NewsEndpointNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
