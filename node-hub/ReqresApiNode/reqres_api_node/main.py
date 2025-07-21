# Dependencies: requests
# To install: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input from other nodes, although not needed for the GET request
    user_input = agent.receive_parameter('user_input')  # Not used directly, added for interface compliance
    try:
        endpoint = "https://reqres.in/api/users?page=1"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()  # Raise error for HTTP failures
        try:
            api_data = response.json()
        except Exception as json_err:
            # JSON parse failed; serialize as text
            api_data = {'error': 'Failed to parse JSON', 'raw_text': response.text}
    except Exception as e:
        api_data = {'error': str(e)}
    # Output must be serializable
    agent.send_output(
        agent_output_name='api_response',
        agent_result=api_data
    )

def main():
    agent = MofaAgent(agent_name='ReqresApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
