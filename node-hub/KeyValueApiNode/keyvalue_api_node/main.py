# Dependencies: requests
# Make sure to install requests: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate calls from other nodes, even though no input is required:
    user_input = agent.receive_parameter('user_input')

    set_endpoint = 'https://api.keyval.org/set/scientist/einstein'
    get_endpoint = 'https://api.keyval.org/get/scientist/'
    responses = {}

    try:
        # Set Value via GET
        set_resp = requests.get(set_endpoint)
        responses['set_status_code'] = set_resp.status_code
        try:
            responses['set_response'] = set_resp.json()
        except Exception:
            responses['set_response'] = set_resp.text
    except Exception as e:
        responses['set_error'] = str(e)

    try:
        # Get Value via GET
        get_resp = requests.get(get_endpoint)
        responses['get_status_code'] = get_resp.status_code
        try:
            responses['get_response'] = get_resp.json()
        except Exception:
            responses['get_response'] = get_resp.text
    except Exception as e:
        responses['get_error'] = str(e)

    agent.send_output(
        agent_output_name='api_results',
        agent_result=responses
    )

def main():
    agent = MofaAgent(agent_name='KeyValueApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()