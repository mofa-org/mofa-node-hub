"""
Dependencies:
- requests

No inputs are required for this agent. To allow consistent dataflow, a placeholder input `user_input` is expected (though ignored), so other nodes can trigger this agent.
"""

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Placeholder input handling, allows node trigger in pipeline
    user_input = agent.receive_parameter('user_input')
    api_endpoint = 'https://api.worldbank.org/v2/region?format=json'
    try:
        response = requests.get(api_endpoint, timeout=10)
        response.raise_for_status()
        # World Bank API returns JSON, but sometimes double-list: [metadata, results]
        data = response.json()
        # Ensure JSON is serializable (dict or list)
        agent.send_output(
            agent_output_name='regions',
            agent_result=data
        )
    except Exception as e:
        err_msg = {'error': True, 'message': str(e)}
        agent.send_output(
            agent_output_name='regions',
            agent_result=err_msg
        )

def main():
    agent = MofaAgent(agent_name='WorldBankRegionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
