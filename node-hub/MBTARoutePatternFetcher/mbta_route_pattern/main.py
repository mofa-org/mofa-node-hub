from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Even if no input required, facilitate call from other nodes
    user_input = agent.receive_parameter('user_input')

    endpoint = "https://api-v3.mbta.com/route_patterns?filter[route]=CR-Providence&include=representative_trip&fields[trip]=headsign"
    timeout = 30  # default timeout (can be made configurable)
    result = None
    try:
        response = requests.get(endpoint, timeout=timeout)
        response.raise_for_status()  # HTTP error handling
        # Ensure response is serializable
        try:
            result = response.json()
        except Exception as json_err:
            result = {'error': 'Failed to parse JSON', 'details': str(json_err)}
    except requests.RequestException as req_err:
        result = {'error': 'HTTP Request failed', 'details': str(req_err)}
    except Exception as e:
        result = {'error': 'Unexpected error', 'details': str(e)}

    agent.send_output(
        agent_output_name='route_patterns',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='MBTARoutePatternFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
