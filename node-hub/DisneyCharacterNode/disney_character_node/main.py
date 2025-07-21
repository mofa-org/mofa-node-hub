from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    DisneyCharacterNode Agent:
    - input_port: action (str: 'by_id' | 'by_name' | 'all')
    - input_port: value (str: id or character name, required for 'by_id' and 'by_name')
    output_port: result (dict or str) -- API response or error details
    """
    try:
        params = agent.receive_parameters(['action', 'value'])
        action = params.get('action', '').strip().lower()
        value = params.get('value', '').strip()
        base_url = "https://api.disneyapi.dev"
        timeout = 30

        if action == 'by_id':
            if not value:
                raise ValueError('Missing id for by_id action.')
            endpoint = f"{base_url}/character/{value}"
            response = requests.get(endpoint, timeout=timeout)
            response.raise_for_status()
            agent.send_output(
                agent_output_name='result',
                agent_result=response.json()
            )

        elif action == 'by_name':
            if not value:
                raise ValueError('Missing name for by_name action.')
            endpoint = f"{base_url}/character"
            response = requests.get(endpoint, params={'name': value}, timeout=timeout)
            response.raise_for_status()
            agent.send_output(
                agent_output_name='result',
                agent_result=response.json()
            )

        elif action == 'all':
            endpoint = f"{base_url}/character"
            response = requests.get(endpoint, timeout=timeout)
            response.raise_for_status()
            agent.send_output(
                agent_output_name='result',
                agent_result=response.json()
            )
        else:
            raise ValueError('Invalid action. Use "by_id", "by_name", or "all".')
    except Exception as e:
        agent.send_output(
            agent_output_name='result',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='DisneyCharacterNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
# Dependencies:
# - requests
# To install: pip install requests
#
# Usage:
# Input ports: action, value (both string, value required only for by_id and by_name)
# Example action inputs for API usage:
#   by_id  (value="1")     -> character with id 1
#   by_name (value="Mickey Mouse") -> search by name
#   all     (value unused)  -> returns all characters (may be paginated)
"""