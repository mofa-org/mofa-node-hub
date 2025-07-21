from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate dataflow consistency even without inputs
    user_input = agent.receive_parameter('user_input')
    api_url = "https://api.jsoning.com/mock/public/products"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # Ensure result is serializable (usually JSON)
        result = response.json()
    except Exception as e:
        result = {'error': True, 'message': str(e)}
    agent.send_output(
        agent_output_name='api_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='MockAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()
