# Dependencies:
#   - requests
#   - mofa
# Ensure 'requests' is in your requirements.txt or environment

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # This node does not require any input, but for compatibility, receive a placeholder input
    user_input = agent.receive_parameter('user_input')

    api_url = "https://api.cepik.gov.pl/version"
    output_port = 'api_version_response'
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # Try to parse JSON, fallback to text
        try:
            out_data = response.json()
        except Exception:
            out_data = response.text
        # Ensure output is serializable (JSON or string)
        agent.send_output(
            agent_output_name=output_port,
            agent_result=out_data
        )
    except Exception as e:
        # Always return error as string in a dict for consistent serialization
        agent.send_output(
            agent_output_name=output_port,
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ApiVersionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
