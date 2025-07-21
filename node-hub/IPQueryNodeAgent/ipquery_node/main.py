from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Always attempt to receive an input to facilitate chaining, even if not needed for this API
    user_input = agent.receive_parameter('user_input')  # Not used, but required by convention
    
    # Configuration
    endpoint = "https://api.ipquery.io/?format=json"

    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Ensure response is JSON serializable
        result = response.json()
        agent.send_output(
            agent_output_name='ipquery_response',
            agent_result=result
        )
    except Exception as e:
        # Contain all errors, respond with a serializable error object
        agent.send_output(
            agent_output_name='ipquery_response',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='IPQueryNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Description: This agent calls the IPQuery API and returns a JSON dictionary with the result. It explicitly receives a dummy user_input parameter for flow consistency with Dora-rs chaining. Errors are caught and returned as serializable dictionaries.
"""