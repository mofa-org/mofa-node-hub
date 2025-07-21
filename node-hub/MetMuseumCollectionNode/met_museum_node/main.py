from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    MetMuseumCollectionNode: Retrieve departments or search objects from the Metropolitan Museum of Art.
    Expected input:
        action: 'departments' or 'search'
        (if action is 'search', provide 'query' for the search string)
    """
    try:
        # Receive required parameters
        params = agent.receive_parameters(['action', 'query'])
        action = params.get('action', '').strip().lower()
        query = params.get('query', '').strip()
        
        output_data = None
        if action == 'departments':
            # Fetch all departments
            url = 'https://collectionapi.metmuseum.org/public/collection/v1/departments'
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            output_data = resp.json()
            agent.send_output('departments', output_data)
        elif action == 'search' and query:
            # Search the collection
            url = f'https://collectionapi.metmuseum.org/public/collection/v1/search'
            resp = requests.get(url, params={'q': query}, timeout=10)
            resp.raise_for_status()
            output_data = resp.json()
            agent.send_output('search_results', output_data)
        else:
            agent.send_output('error', {'message': 'Invalid action or missing query'})
    except Exception as e:
        # Error handling within Agent boundaries
        agent.send_output('error', {'message': str(e)})

def main():
    agent = MofaAgent(agent_name='MetMuseumCollectionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Usage:
- To get all departments:
    action: 'departments'
    query: '' (or any value, ignored)
    Output port: 'departments'
- To search the collection:
    action: 'search'
    query: <search term>
    Output port: 'search_results'
All errors are output to agent_output_name 'error'.
"""