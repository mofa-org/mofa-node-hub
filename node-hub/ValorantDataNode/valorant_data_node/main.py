# Dependencies: requests
# To use this agent, ensure you have 'requests' installed: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input reception for compatibility (even if not used)
    user_input = agent.receive_parameter('user_input')
    outputs = {}
    try:
        # First API: Valorant Buddies
        buddies_resp = requests.get('https://valorant-api.com/v1/buddies', timeout=10)
        buddies_resp.raise_for_status()
        buddies_data = buddies_resp.json()
        outputs['buddies'] = buddies_data
    except Exception as e:
        outputs['buddies'] = {'error': f'Failed to retrieve buddies: {str(e)}'}

    try:
        # Second API: Valorant Agents
        agents_resp = requests.get('https://valorant-api.com/v1/agents', timeout=10)
        agents_resp.raise_for_status()
        agents_data = agents_resp.json()
        outputs['agents'] = agents_data
    except Exception as e:
        outputs['agents'] = {'error': f'Failed to retrieve agents: {str(e)}'}

    # Ensure output is serializable
    agent.send_output(
        agent_output_name='valorant_data',
        agent_result=outputs
    )

def main():
    agent = MofaAgent(agent_name='ValorantDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
