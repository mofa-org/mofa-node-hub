from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Dummy receive to facilitate chaining; not required for this API
    user_input = agent.receive_parameter('user_input')

    api_url = "https://www.healthcare.gov/api/index.json"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        # Output is JSON-serializable dict
        agent.send_output(
            agent_output_name='api_response',
            agent_result=data
        )
    except Exception as e:
        # Error is serialized as str for output
        agent.send_output(
            agent_output_name='api_response',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='HealthcareContentNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests
Install via: pip install requests
"""