from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    Agent for querying Zurich public foot traffic data endpoints.
    Input:
        operation (str): possible values:
            - 'search_jones' (returns search results for 'jones')
            - 'fetch_latest' (returns latest 5 entries, desc order)
    Output:
        output_port: dict with query result, or error info
    """
    try:
        params = agent.receive_parameters(['operation'])  # expects str: 'search_jones' or 'fetch_latest'
        operation = params.get('operation', '').strip()

        if operation == 'search_jones':
            url = 'https://data.stadt-zuerich.ch/api/3/action/datastore_search?resource_id=ec1fc740-8e54-4116-aab7-3394575b4666&q=jones'
        elif operation == 'fetch_latest':
            url = 'https://data.stadt-zuerich.ch/api/3/action/datastore_search?resource_id=ec1fc740-8e54-4116-aab7-3394575b4666&limit=5&sort=timestamp%20desc'
        else:
            agent.send_output(
                agent_output_name='output_port',
                agent_result={"error": True, "message": f"Invalid operation: {operation}"}
            )
            return

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Ensure result is serializable
        data = response.json()
        agent.send_output(
            agent_output_name='output_port',
            agent_result=data
        )

    except Exception as e:
        agent.send_output(
            agent_output_name='output_port',
            agent_result={"error": True, "message": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ZurichFootTrafficNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
