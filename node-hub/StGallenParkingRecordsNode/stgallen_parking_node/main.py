# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    This agent retrieves parking records from the Stadt St.Gallen open data API.
    Accepts optional URL query parameters as a string (e.g., 'limit=10&phname=SomeParkingLot').
    Outputs the API JSON response (results from the endpoint).
    """
    try:
        # Always receive a parameter for framework compatibility
        user_input = agent.receive_parameter('user_input')  # String of extra query params (or empty)
        
        base_url = "https://daten.stadt.sg.ch/api/explore/v2.1/catalog/datasets/freie-parkplatze-in-der-stadt-stgallen-pls/records"
        
        # Default limit
        params = {'limit': '20'}
        
        if user_input:
            # Allow override/additional query parameters via user_input (format: 'key1=val1&key2=val2')
            from urllib.parse import parse_qsl
            try:
                user_params = dict(parse_qsl(user_input))
                params.update(user_params)
            except Exception as e:
                agent.send_output(
                    agent_output_name='api_error',
                    agent_result=f"Parameter parsing error: {str(e)}"
                )
                return
        
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            # Ensure response is serializable (JSON dict)
            agent.send_output(
                agent_output_name='parking_records',
                agent_result=response.json()
            )
        else:
            agent.send_output(
                agent_output_name='api_error',
                agent_result=f"API request failed with status {response.status_code}: {response.text[:200]}"
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='agent_error',
            agent_result=f"Agent runtime error: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='StGallenParkingRecordsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
