from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests (ensure present in requirements)

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitates other nodes to call this agent (stateless design)
        user_input = agent.receive_parameter('user_input')
        # No input required, but enforce input handling pattern
        
        # Endpoint 1: Select fields 'id', 'name', 'href' for all city bike networks
        response_fields = requests.get(
            'http://api.citybik.es/v2/networks?fields=id,name,href', timeout=15
        )
        response_fields.raise_for_status()
        data_fields = response_fields.json()
        # Validate serializability
        if not isinstance(data_fields, (dict, list)):
            raise ValueError('Response is not JSON serializable')
        agent.send_output(
            agent_output_name='selected_fields_networks',
            agent_result=data_fields
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='selected_fields_networks',
            agent_result={'error': str(e)}
        )
    
    try:
        # Endpoint 2: Fetch full city bike networks worldwide
        response_all = requests.get(
            'http://api.citybik.es/v2/networks', timeout=15
        )
        response_all.raise_for_status()
        data_all = response_all.json()
        if not isinstance(data_all, (dict, list)):
            raise ValueError('Response is not JSON serializable')
        agent.send_output(
            agent_output_name='all_networks',
            agent_result=data_all
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='all_networks',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CityBikeNetworksNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
