# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# No API key required according to the documentation.

@run_agent
def run(agent: MofaAgent):
    try:
        # For consistent integration in a dataflow, allow input param
        user_input = agent.receive_parameter('user_input')
        # Endpoint for latest USD exchange rates
        endpoint = 'https://open.er-api.com/v6/latest/USD'
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()  # Handles HTTP errors
        data = response.json()
        # Ensure output can be serialized (convert non-serializable types if any)
        agent.send_output(
            agent_output_name='exchange_rate_data',
            agent_result=data
        )
    except Exception as e:
        # Provide error details in output, but do not raise exception
        agent.send_output(
            agent_output_name='exchange_rate_data',
            agent_result={'error': True, 'message': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ExchangeRateAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()
