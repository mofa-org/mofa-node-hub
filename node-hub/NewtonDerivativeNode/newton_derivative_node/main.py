from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate calls from other nodes, even if no input is required
    user_input = agent.receive_parameter('user_input')
    try:
        # Endpoint is fixed; no request parameters needed
        endpoint = "https://newton.now.sh/api/v2/derive/x%5E2"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        try:
            api_result = response.json()
        except Exception:
            # Fallback if not valid JSON
            api_result = {'result': response.text}
        # Validate output is serializable
        agent.send_output(
            agent_output_name='derivative_output',
            agent_result=api_result
        )
    except Exception as e:
        # Error containment - send error as output
        error_result = {'error': str(e)}
        agent.send_output(
            agent_output_name='derivative_output',
            agent_result=error_result
        )

def main():
    agent = MofaAgent(agent_name='NewtonDerivativeNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
