from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate other nodes to call it even if no input is required
        user_input = agent.receive_parameter('user_input')  # Ignored in logic

        # API endpoint
        endpoint = "https://phish.in/api/v2/shows"

        # Execute HTTP GET request
        response = requests.get(endpoint, timeout=15)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Attempt to parse JSON
        try:
            data = response.json()
        except Exception as json_err:
            # Fallback: treat as text if not valid json
            data = {'error': 'Invalid JSON response', 'details': str(json_err), 'raw_content': response.text}

        # Ensure output is serializable (dict)
        agent.send_output(
            agent_output_name='phish_show_data',
            agent_result=data
        )
    except Exception as e:
        error_message = {'error': 'Failed to fetch Phish shows', 'details': str(e)}
        agent.send_output(
            agent_output_name='phish_show_data',
            agent_result=error_message
        )

def main():
    agent = MofaAgent(agent_name='PhishApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
