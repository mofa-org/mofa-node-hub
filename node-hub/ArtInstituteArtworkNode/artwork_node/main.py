# Dependencies:
#   requests
# Please ensure the requests library is available in your environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

API_BASE = "https://api.artic.edu/api/v1/artworks"

@run_agent
def run(agent: MofaAgent):
    try:
        # Accepts action_type parameter (string):
        #   'get_specific' - image of a specific artwork (id=27992)
        #   'get_all'      - retrieve all artworks
        #   'search'       - search for artworks with cats
        
        # To facilitate graph connections, always receive user_input (not used)
        user_input = agent.receive_parameter('user_input')  # Placeholder for dataflow
        action_type = agent.receive_parameter('action_type')
        
        if not isinstance(action_type, str):
            raise ValueError("Parameter 'action_type' must be a string.")

        headers = {"Accept": "application/json"}

        if action_type == 'get_specific':
            endpoint = f"{API_BASE}/27992?fields=id,title,image_id"
            resp = requests.get(endpoint, headers=headers, timeout=10)
        elif action_type == 'get_all':
            endpoint = API_BASE
            resp = requests.get(endpoint, headers=headers, timeout=10)
        elif action_type == 'search':
            endpoint = f"{API_BASE}/search?q=cats"
            resp = requests.get(endpoint, headers=headers, timeout=10)
        else:
            raise ValueError(f"Unknown action_type: {action_type}")

        if resp.status_code != 200:
            agent.send_output(
                agent_output_name='artwork_data',
                agent_result={
                    'error': True,
                    'status_code': resp.status_code,
                    'message': 'Request failed',
                    'details': resp.text,
                }
            )
            return

        try:
            result_data = resp.json()
        except Exception as json_exc:
            agent.send_output(
                agent_output_name='artwork_data',
                agent_result={
                    'error': True,
                    'status_code': resp.status_code,
                    'message': 'Invalid JSON response',
                    'details': str(json_exc),
                }
            )
            return

        agent.send_output(
            agent_output_name='artwork_data',
            agent_result=result_data
        )

    except Exception as e:
        agent.send_output(
            agent_output_name='artwork_data',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='ArtInstituteArtworkNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
