from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependency: requests
# Ensure in requirements: requests>=2.0.0

OPENVERSE_API_ENDPOINT = "https://api.openverse.org/v1/images/"
DEFAULT_QUERY = "dog"
DEFAULT_FORMAT = "json"
DEFAULT_TIMEOUT = 30
DEFAULT_MAX_RESULTS = 10

@run_agent
def run(agent: MofaAgent):
    # To facilitate dataflow even if not used
    user_input = agent.receive_parameter('user_input')
    # This agent does not require specific input, but to comply with dora-rs pattern, we allow pass-through

    try:
        params = {
            "format": DEFAULT_FORMAT,
            "q": DEFAULT_QUERY,
            "page_size": str(DEFAULT_MAX_RESULTS)
        }
        response = requests.get(
            OPENVERSE_API_ENDPOINT,
            params=params,
            timeout=DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()
        # Only send a summary of results (list of URLs and descriptions)
        results = []
        for item in data.get('results', []):
            results.append({
                'id': item.get('id'),
                'title': item.get('title'),
                'url': item.get('url'),
                'thumbnail': item.get('thumbnail'),
                'description': item.get('description'),
            })
        agent.send_output(
            agent_output_name='openverse_images',
            agent_result=results
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='openverse_images',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='OpenverseImageSearchNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
