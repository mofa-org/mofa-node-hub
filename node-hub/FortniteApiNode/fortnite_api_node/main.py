from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# No input required. To facilitate other nodes to call this agent:
def fetch_fortnite_api_data():
    endpoints = {
        'cosmetics': 'https://fortnite-api.com/v2/cosmetics',
        'map': 'https://fortnite-api.com/v1/map',
        'playlists': 'https://fortnite-api.com/v1/playlists'
    }
    results = {}
    errors = {}

    for key, url in endpoints.items():
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            # Try to parse JSON, use text fallback
            try:
                results[key] = response.json()
            except Exception:
                results[key] = response.text
        except Exception as e:
            errors[key] = str(e)

    return {'results': results, 'errors': errors}

@run_agent
def run(agent: MofaAgent):
    # No parameters required, but to allow port composition:
    user_input = agent.receive_parameter('user_input')
    try:
        data = fetch_fortnite_api_data()
        # Output will contain 'results' and 'errors' for transparency
        agent.send_output(
            agent_output_name='fortnite_api_data',
            agent_result=data  # Dict, serializable
        )
    except Exception as e:
        # Fatal agent error, encapsulate
        agent.send_output(
            agent_output_name='fortnite_api_data',
            agent_result={'results': {}, 'errors': {'agent': str(e)}}
        )

def main():
    agent = MofaAgent(agent_name='FortniteApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
