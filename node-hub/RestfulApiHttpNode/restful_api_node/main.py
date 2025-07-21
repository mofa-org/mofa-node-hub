# Dependencies: requests
# Add to requirements.txt: requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # Facilitate call chaining; not used here
    api_endpoint = "https://api.restful-api.dev/objects"
    try:
        response = requests.get(api_endpoint, timeout=10)
        response.raise_for_status()  # Raise error for non-2xx responses
        try:
            data = response.json()  # Expect the API to return JSON
        except Exception as e:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={
                    'error': 'Failed to decode response as JSON',
                    'exception': str(e),
                    'response_text': response.text
                }
            )
            return
        # Send JSON response
        agent.send_output(
            agent_output_name='api_response',
            agent_result=data
        )
    except requests.RequestException as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': 'HTTP Request failed',
                'exception': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='RestfulApiHttpNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
