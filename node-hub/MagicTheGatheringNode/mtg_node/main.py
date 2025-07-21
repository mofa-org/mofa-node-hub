from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Input handling: Get 'resource_type' parameter
    try:
        resource_type = agent.receive_parameter('resource_type')  # expects 'cards' or 'sets'
        resource_type = str(resource_type).strip().lower()
        
        # Optional: receive query string for more flexible API queries
        query = agent.receive_parameter('query')  # expects a query like '?name=Llanowar Elves', or ''
        if query is not None:
            query = str(query)
            if len(query.strip()) > 0 and not query.startswith('?'):
                query = '?' + query.strip()
        else:
            query = ''
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={'error': f'Failed to receive inputs: {str(e)}'}
        )
        return

    # Map resource_type to endpoint
    base_url = 'https://api.magicthegathering.io/v1/'
    if resource_type not in ('cards', 'sets'):
        agent.send_output(
            agent_output_name='api_response',
            agent_result={'error': 'Invalid resource_type. Must be "cards" or "sets".'}
        )
        return
    endpoint = base_url + resource_type + query

    # Call MTG API
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        # Ensure serialization for output (dict is allowed)
        agent.send_output(
            agent_output_name='api_response',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={'error': f'API call failed: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='MagicTheGatheringNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
