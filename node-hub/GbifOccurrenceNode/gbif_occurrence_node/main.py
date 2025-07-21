# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

def fetch_gbif_occurrences():
    """
    Requests GBIF occurrence data for the years 1800 to 1899.
    Returns: dict on success
    Raises: Exception on failure
    """
    endpoint = "https://api.gbif.org/v1/occurrence/search?year=1800,1899"
    try:
        resp = requests.get(endpoint, timeout=30)
        resp.raise_for_status()
        # Only include JSON-serializable output
        data = resp.json()
        return data
    except Exception as e:
        # Raise for outer error handling
        raise Exception(f"GBIF API request failed: {e}")

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes to call this agent,
    # receive a dummy string input parameter.
    user_input = agent.receive_parameter('user_input')
    try:
        gbif_data = fetch_gbif_occurrences()
        # Always ensure JSON-serializability
        agent.send_output(
            agent_output_name='gbif_occurrence_output',
            agent_result=gbif_data
        )
    except Exception as err:
        # Error is contained and returned in a serializable format
        agent.send_output(
            agent_output_name='gbif_occurrence_output',
            agent_result={"error": True, "message": str(err)}
        )

def main():
    agent = MofaAgent(agent_name='GbifOccurrenceNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
