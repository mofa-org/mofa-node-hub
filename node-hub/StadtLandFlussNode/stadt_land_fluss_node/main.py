from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes to call this agent, we add a dummy input parameter
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://slftool.github.io/data.json', timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure the output is serializable
        agent.send_output(
            agent_output_name='stadt_land_fluss_data',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='stadt_land_fluss_data',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='StadtLandFlussNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
