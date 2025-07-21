from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it even if not required
    user_input = agent.receive_parameter('user_input')  # Not used further - compliance only

    try:
        # Lookup banana information
        banana_url = 'https://www.fruityvice.com/api/fruit/banana'
        banana_resp = requests.get(banana_url, timeout=10)
        banana_resp.raise_for_status()
        banana_result = banana_resp.json()
    except Exception as e:
        banana_result = {'error': f'Failed to fetch banana info: {str(e)}'}

    try:
        # Lookup all fruits information
        all_url = 'https://www.fruityvice.com/api/fruit/all'
        all_resp = requests.get(all_url, timeout=10)
        all_resp.raise_for_status()
        all_result = all_resp.json()
    except Exception as e:
        all_result = {'error': f'Failed to fetch all fruits info: {str(e)}'}

    # Output delivery; names are consistent with data flow needs
    agent.send_output(
        agent_output_name='banana_info',
        agent_result=banana_result
    )
    agent.send_output(
        agent_output_name='all_fruits_info',
        agent_result=all_result
    )

def main():
    agent = MofaAgent(agent_name='FruitLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
