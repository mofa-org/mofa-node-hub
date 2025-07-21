from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Faciliate call by other nodes, even though no input is required
    user_input = agent.receive_parameter('user_input')

    # Data.gov endpoints
    endpoints = [
        "https://catalog.data.gov/api/3/action/package_search",
        "https://catalog.data.gov/api/3/action/group_list",
    ]
    results = {}
    for url in endpoints:
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            # Only deliver json-serializable
            data = resp.json()
            results[url] = data
        except Exception as e:
            results[url] = {"error": str(e)}

    # Output to dataflow port "data_gov_results"
    agent.send_output(
        agent_output_name='data_gov_results',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='DataGovNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# Ensure 'requests' is included in your environment or requirements.txt.
