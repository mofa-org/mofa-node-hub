from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# No input is required, but include user_input for framework compatibility
def fetch_endpoint_data(endpoint_url: str, timeout: int = 30):
    try:
        response = requests.get(endpoint_url, timeout=timeout)
        response.raise_for_status()
        # Ensure data is serializable (JSON)
        return response.json()
    except Exception as e:
        return {"error": str(e), "endpoint": endpoint_url}

@run_agent
def run(agent: MofaAgent):
    # Compatibility input (stateless design; not used here)
    user_input = agent.receive_parameter('user_input')
    
    base_url = "https://sepomex.icalialabs.com/api/v1/"
    endpoints = {
        "municipalities": "municipalities",
        "zip_codes": "zip_codes",
        "states": "states",
        "cities": "cities"
    }
    timeout = 30

    results = {}
    for name, endpoint in endpoints.items():
        endpoint_url = base_url + endpoint
        data = fetch_endpoint_data(endpoint_url, timeout=timeout)
        results[name] = data
    # Output results to standard port name
    agent.send_output(
        agent_output_name='zipcode_api_data',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='MexicanZipCodeApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
