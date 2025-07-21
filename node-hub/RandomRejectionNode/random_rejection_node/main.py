from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # This agent does not require any input, but we receive a dummy input to maintain dataflow compatibility
    user_input = agent.receive_parameter('user_input')

    endpoint = "https://naas.isalman.dev/no"
    timeout = 5
    try:
        response = requests.get(endpoint, timeout=timeout)
        response.raise_for_status()
        # Ensure the output is serializable (as str or dict)
        try:
            result = response.json()
        except Exception:
            result = response.text
        
        agent.send_output(
            agent_output_name='random_rejection_reason',
            agent_result=result
        )
    except Exception as e:
        error_message = {
            "error": "Failed to fetch random rejection reason.",
            "detail": str(e)
        }
        agent.send_output(
            agent_output_name='random_rejection_reason',
            agent_result=error_message
        )

def main():
    agent = MofaAgent(agent_name='RandomRejectionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
