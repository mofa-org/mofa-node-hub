from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    """
    dora-rs compliant Agent for querying status of parking garages in Zurich and Basel.
    Configurable via endpoints; fetches data from the provided APIs and outputs the results.
    """
    try:
        # Facilitate other nodes to call it, even though there is no required input
        user_input = agent.receive_parameter('user_input')

        # Endpoints can be loaded from config or hardcoded
        endpoints = [
            'https://api.parkendd.de/Zuerich',
            'https://api.parkendd.de/Basel'
        ]
        timeout = 30  # seconds (can be modified with env or config if desired)

        results = []
        for url in endpoints:
            try:
                resp = requests.get(url, timeout=timeout)
                resp.raise_for_status()
                data = resp.json()
                # Ensure the JSON result is serializable
                results.append({'endpoint': url, 'data': data})
            except requests.RequestException as e:
                # Handle connection/timeout/HTTP errors for individual endpoints
                results.append({'endpoint': url, 'error': str(e)})
            except Exception as e:
                # Handle unexpected errors for this endpoint
                results.append({'endpoint': url, 'error': f'Unexpected error: {str(e)}'})

        # Send all results as the dataflow output; list of dicts is serializable
        agent.send_output(
            agent_output_name='parking_statuses',
            agent_result=results
        )
    except Exception as e:
        # Critical error handling; sends as error message for the entire agent
        agent.send_output(
            agent_output_name='parking_statuses',
            agent_result={'error': f'Agent encountered a fatal error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='ParkingStatusNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
