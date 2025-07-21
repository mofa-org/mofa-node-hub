# Dependencies: requests
# No environment variables required since API endpoint takes no parameters and is open.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # No specified input parameter. To facilitate integration, receive a dummy user_input.
        user_input = agent.receive_parameter('user_input')
        api_endpoint = 'https://financialdata.net/documentation'
        response = requests.get(api_endpoint, timeout=10)
        # Ensure serialization
        try:
            response_data = response.json()
        except Exception:
            response_data = response.text
        agent.send_output(
            agent_output_name='financial_data_response',
            agent_result=response_data
        )
    except Exception as e:
        # Handle all error cases and send a serializable error message
        agent.send_output(
            agent_output_name='financial_data_response',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='FinancialDataConnectorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
