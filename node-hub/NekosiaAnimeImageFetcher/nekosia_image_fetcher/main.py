from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# List of nekosia image API endpoints with mapped categories
ekosia_endpoints = {
    "tail-with-ribbon": "https://api.nekosia.cat/api/v1/images/tail-with-ribbon",
    "foxgirl": "https://api.nekosia.cat/api/v1/images/foxgirl",
    "maid": "https://api.nekosia.cat/api/v1/images/maid",
    "vtuber": "https://api.nekosia.cat/api/v1/images/vtuber",
    "thigh-high-socks": "https://api.nekosia.cat/api/v1/images/thigh-high-socks",
    "cute": "https://api.nekosia.cat/api/v1/images/cute",
    "catgirl": "https://api.nekosia.cat/api/v1/images/catgirl"
}

@run_agent
def run(agent: MofaAgent):
    # Receives 'category' from upstream as string input
    user_input = agent.receive_parameter('category')
    category = user_input.strip().lower()
    result = {}
    if category not in nekosia_endpoints:
        result = {
            "error": True,
            "message": f"Unknown category '{{category}}'. Choose one of: {{', '.join(nekosia_endpoints.keys())}}."
        }
        agent.send_output(agent_output_name='image_result', agent_result=result)
        return
    url = nekosia_endpoints[category]
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        # The Nekosia API returns image info (usually a JSON dict with image url)
        data = resp.json()
        result = {"error": False, "data": data, "category": category}
    except requests.exceptions.RequestException as e:
        result = {
            "error": True,
            "message": f"Failed to fetch image from Nekosia for category '{{category}}': {{str(e)}}"
        }
    except Exception as e:
        result = {
            "error": True,
            "message": f"Unexpected error: {{str(e)}}"
        }
    # Must be serializable (dict guaranteed)
    agent.send_output(agent_output_name='image_result', agent_result=result)

def main():
    agent = MofaAgent(agent_name='NekosiaAnimeImageFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Requirements (place in requirements.txt):
# requests>=2.25.0
