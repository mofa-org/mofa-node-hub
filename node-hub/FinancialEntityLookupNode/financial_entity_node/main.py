# Dependencies: requests
# Install: pip install requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate dataflow and interoperability, always expect an input (even if unused)
    user_input = agent.receive_parameter('user_input')  # Accepts input to maintain interface consistency
    try:
        endpoint = "https://entitydb.shodan.io/api/entities/symbol/GOOG"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        try:
            result_data = response.json()
        except Exception:
            # Not a JSON response, fallback to text
            result_data = response.text
        # Ensure the data is serializable (dict or str)
        if not isinstance(result_data, (str, dict, list)):
            result_data = str(result_data)
        agent.send_output(
            agent_output_name='financial_data',
            agent_result=result_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='financial_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='FinancialEntityLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
