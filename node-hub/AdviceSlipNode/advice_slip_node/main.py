from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to provide input (even if not needed by this agent)
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://api.adviceslip.com/advice/search/try1', timeout=10)
        response.raise_for_status()
        # The API returns JSON, try to parse it
        data = response.json()
        # Ensure output is serializable (dict)
        agent.send_output(
            agent_output_name='advice_slip_response',
            agent_result=data
        )
    except Exception as e:
        # Handle and report errors
        agent.send_output(
            agent_output_name='advice_slip_response',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='AdviceSlipNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
