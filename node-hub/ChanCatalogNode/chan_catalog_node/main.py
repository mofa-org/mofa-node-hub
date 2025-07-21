# Requirements (must be declared in your project):
#   requests>=2.31.0
#
# Environment/Secret config: None required for this agent

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Fetches data from three 4chan endpoints and outputs their JSON content via respective dataflow ports. 
    Input call placeholder (for chaining): always receives 'user_input', but does not use it.
    Outputs:
      - origami_catalog: Catalog from Origami board (/po/)
      - three_d_catalog: Catalog from 3D board (/3/)
      - boards: List of all boards
    """
    user_input = agent.receive_parameter('user_input')  # For dataflow compatibility, not used here

    endpoints = {
        'origami_catalog': 'https://a.4cdn.org/po/catalog.json',
        'three_d_catalog': 'https://a.4cdn.org/3/catalog.json',
        'boards': 'https://a.4cdn.org/boards.json',
    }

    for port, url in endpoints.items():
        try:
            resp = requests.get(url, timeout=12)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            # Structured error message for easy debugging downstream
            data = {'error': True, 'message': str(e), 'endpoint': url}
        agent.send_output(
            agent_output_name=port,
            agent_result=data
        )

def main():
    agent = MofaAgent(agent_name='ChanCatalogNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
