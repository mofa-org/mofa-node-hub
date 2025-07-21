from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input for framework chaining, even if not required
    user_input = agent.receive_parameter('user_input')
    try:
        api_url = "https://get.uptime.is/api"
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The API may return JSON or plain text
        try:
            api_result = response.json()
        except Exception:
            api_result = response.text  # fallback if not JSON
        # Ensure result is serializable
        agent.send_output(
            agent_output_name='uptime_api_result',
            agent_result=api_result
        )
    except Exception as e:
        # Contain all potential errors
        agent.send_output(
            agent_output_name='uptime_api_result',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='UptimeApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   - requests: For API HTTP access (add to requirements)
