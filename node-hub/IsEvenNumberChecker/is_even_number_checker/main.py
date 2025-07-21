from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive user input as string (for stateless compliance)
        user_input = agent.receive_parameter('user_input')
        # Convert to int if possible, else raise error
        try:
            number = int(user_input)
        except (ValueError, TypeError):
            agent.send_output(
                agent_output_name='is_even_api_response',
                agent_result={
                    'error': True,
                    'message': 'Input must be an integer-representable string.'
                }
            )
            return

        # Endpoint from config or default (hardcoded for agent packaging)
        endpoint = f"https://api.isevenapi.xyz/api/iseven/{number}/"

        # Perform API request
        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='is_even_api_response',
                agent_result={
                    'error': True,
                    'message': f'API call failed: {str(e)}'
                }
            )
            return

        # Only forward serializable response
        agent.send_output(
            agent_output_name='is_even_api_response',
            agent_result=data
        )
    except Exception as general_error:
        # Catch all unforeseen errors
        agent.send_output(
            agent_output_name='is_even_api_response',
            agent_result={
                'error': True,
                'message': f'Unexpected error in agent: {str(general_error)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='IsEvenNumberChecker')
    run(agent=agent)

if __name__ == '__main__':
    main()
