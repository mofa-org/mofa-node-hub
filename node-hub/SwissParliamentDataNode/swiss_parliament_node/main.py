from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

def fetch_swiss_parliament_data(endpoint_url: str, timeout: int = 10):
    try:
        response = requests.get(endpoint_url, timeout=timeout)
        response.raise_for_status()
        # Parsing as JSON to ensure serializability
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}

@run_agent
def run(agent: MofaAgent):
    """
    Dataflow input:
      - No specific input needed, but include user_input = agent.receive_parameter('user_input') for framework compatibility.
    Dataflow outputs:
      - 'sessions_data'   : Parliament Sessions
      - 'councillors_data': List of Councillors
      - 'votes_data'      : Votes by Councillor
    """
    # To facilitate other nodes to call it even if no input required:
    user_input = agent.receive_parameter('user_input')

    # Endpoint URLs from config/yml
    SESSIONS_URL = 'https://ws-old.parlament.ch/sessions?lang=en&format=json'
    COUNCILLORS_URL = 'https://ws-old.parlament.ch/councillors/basicdetails?lang=en&format=json'
    VOTES_URL = 'https://ws-old.parlament.ch/votes/councillors?lang=en&format=json'
    TIMEOUT = 10
    # Get Parliament Sessions
    sessions_data = fetch_swiss_parliament_data(SESSIONS_URL, timeout=TIMEOUT)
    agent.send_output(
        agent_output_name='sessions_data',
        agent_result=sessions_data
    )
    # Get Councillors
    councillors_data = fetch_swiss_parliament_data(COUNCILLORS_URL, timeout=TIMEOUT)
    agent.send_output(
        agent_output_name='councillors_data',
        agent_result=councillors_data
    )
    # Get Votes by Councillor
    votes_data = fetch_swiss_parliament_data(VOTES_URL, timeout=TIMEOUT)
    agent.send_output(
        agent_output_name='votes_data',
        agent_result=votes_data
    )

def main():
    agent = MofaAgent(agent_name='SwissParliamentDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
