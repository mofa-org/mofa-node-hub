from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receives 'data_type' parameter to select the endpoint ('characters' or 'combat_styles')
        data_type = agent.receive_parameter('data_type')
        
        # Mapping between data_type and API endpoint
        endpoint_map = {
            'characters': 'https://www.demonslayer-api.com/api/v1/characters',
            'combat_styles': 'https://www.demonslayer-api.com/api/v1/combat-styles',
        }
        
        url = endpoint_map.get(data_type.strip().lower())
        if not url:
            agent.send_output(
                agent_output_name='demon_slayer_data',
                agent_result={
                    'error': f"Invalid data_type '{data_type}'. Choose 'characters' or 'combat_styles'."
                }
            )
            return
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()  # Assumes JSON serializable output
        
        agent.send_output(
            agent_output_name='demon_slayer_data',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='demon_slayer_data',
            agent_result={
                'error': f'Failed to fetch Demon Slayer API data: {str(e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='DemonSlayerDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
