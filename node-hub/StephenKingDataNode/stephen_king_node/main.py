from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependency: requests
# pip install requests

def fetch_stephen_king_data(endpoint_url: str, timeout: int = 30):
    try:
        response = requests.get(endpoint_url, timeout=timeout)
        response.raise_for_status()
        try:
            return response.json()
        except Exception:
            return response.text
    except Exception as e:
        return {"error": str(e)}

@run_agent
def run(agent: MofaAgent):
    # Facilitates API call trigger by other nodes
    user_input = agent.receive_parameter('user_input')  # doesn't affect logic, enables connectivity
    # Endpoints as per configuration
    base_url = "https://stephen-king-api.onrender.com/api"
    endpoints = {
        "books": f"{base_url}/books",
        "villains": f"{base_url}/villains",
        "shorts": f"{base_url}/shorts"
    }
    timeout = 30

    results = {}
    for key, url in endpoints.items():
        results[key] = fetch_stephen_king_data(url, timeout=timeout)

    agent.send_output(
        agent_output_name="stephen_king_data",
        agent_result=results  # Ensures serialization (dict)
    )

def main():
    agent = MofaAgent(agent_name="StephenKingDataNode")
    run(agent=agent)

if __name__ == "__main__":
    main()
