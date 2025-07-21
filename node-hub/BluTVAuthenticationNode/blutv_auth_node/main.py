# Dependencies: requests (install via `pip install requests`)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive a dummy input for node chaining purposes
        user_input = agent.receive_parameter('user_input')
        # Since this endpoint does not require parameters, just perform GET request
        url = "https://www.blutv.com/int/giris"
        response = requests.get(url, timeout=10)

        # Validate HTTP response
        if response.status_code == 200:
            agent.send_output(
                agent_output_name='auth_response',
                agent_result=response.text  # Sending as string (HTML or JSON or text)
            )
        else:
            agent.send_output(
                agent_output_name='auth_response',
                agent_result=f"Error: Received status code {response.status_code}"
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='auth_response',
            agent_result=f"Exception occurred: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='BluTVAuthenticationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
