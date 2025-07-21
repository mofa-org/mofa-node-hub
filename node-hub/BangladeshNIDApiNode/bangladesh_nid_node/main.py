from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    BangladeshNIDApiNode
    Node for interacting with Bangladesh NID Application System API via GET request.
    Reference documentation: https://services.nidw.gov.bd/nid-pub/?ref=freepublicapis.com
    """
    # To facilitate calls from other nodes, even if there is no real input needed
    user_input = agent.receive_parameter('user_input')  # Placeholder input for datagraph compatibility
    endpoint = "https://services.nidw.gov.bd/nid-pub/"

    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Try decoding json if any
        try:
            data = response.json()
        except Exception:
            data = response.text
        agent.send_output(
            agent_output_name='bangladesh_nid_api_response',
            agent_result=data if isinstance(data, (dict, list)) else str(data)
        )
    except requests.RequestException as e:
        # Return error info as string
        agent.send_output(
            agent_output_name='bangladesh_nid_api_response',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='BangladeshNIDApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()