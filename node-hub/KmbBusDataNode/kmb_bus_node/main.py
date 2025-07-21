from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests
#   Ensure this is included in requirements.txt or your environment.
#
# API documentation:
#   https://data.gov.hk/en-data/dataset/hk-td-tis_21-etakmb?ref=freepublicapis.com

@run_agent
def run(agent: MofaAgent):
    """
    Fetches KMB routes and stops from open API.
    Returns both as a dictionary containing two keys: 'routes' and 'stops'.
    This agent is stateless and handles all errors internally.
    """
    # Add a default receive_parameter to facilitate linkage, per requirements.
    user_input = agent.receive_parameter('user_input')

    kmb_routes_url = "https://data.etabus.gov.hk/v1/transport/kmb/route/"
    kmb_stops_url = "https://data.etabus.gov.hk/v1/transport/kmb/stop"

    results = {'routes': None, 'stops': None, 'error': None}

    try:
        # Fetch routes
        resp_routes = requests.get(kmb_routes_url, timeout=8)
        resp_routes.raise_for_status()
        results['routes'] = resp_routes.json()
    except Exception as e:
        results['error'] = f"Failed to fetch KMB routes: {str(e)}"

    try:
        # Fetch stops
        resp_stops = requests.get(kmb_stops_url, timeout=8)
        resp_stops.raise_for_status()
        results['stops'] = resp_stops.json()
    except Exception as e:
        err_str = f"Failed to fetch KMB stops: {str(e)}"
        results['error'] = results['error'] + ' | ' + err_str if results['error'] else err_str

    # Only outputs serializable types (dict)
    agent.send_output(
        agent_output_name='kmb_bus_data',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='KmbBusDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
