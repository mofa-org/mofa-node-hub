# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    DnDApiNodeBridge - Retrieve data from selected D&D 5e API endpoint.
    Required Input: endpoint_choice (str, one of ['dwarf', 'spells', 'ability_scores_cha'])
      - 'dwarf' : https://www.dnd5eapi.co/api/races/dwarf
      - 'spells': https://www.dnd5eapi.co/api/spells
      - 'ability_scores_cha': https://www.dnd5eapi.co/api/ability-scores/cha
    Output: Dict containing API response, serialized.
    """
    try:
        # Receive required parameter for endpoint selection
        endpoint_choice = agent.receive_parameter('endpoint_choice')

        # Map choices to endpoints
        endpoint_map = {
            'dwarf': 'https://www.dnd5eapi.co/api/races/dwarf',
            'spells': 'https://www.dnd5eapi.co/api/spells',
            'ability_scores_cha': 'https://www.dnd5eapi.co/api/ability-scores/cha',
        }
        endpoint_url = endpoint_map.get(endpoint_choice.strip().lower())
        if not endpoint_url:
            agent.send_output(
                agent_output_name='dnd_api_response',
                agent_result={
                    'error': True,
                    'message': f"Invalid endpoint_choice provided: '{endpoint_choice}'"
                }
            )
            return
        # Call the API endpoint (GET, no parameters needed)
        resp = requests.get(endpoint_url, timeout=10)
        try:
            resp.raise_for_status()
        except Exception as e:
            agent.send_output(
                agent_output_name='dnd_api_response',
                agent_result={'error': True, 'message': f'HTTP error: {str(e)}'}
            )
            return
        try:
            response_json = resp.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='dnd_api_response',
                agent_result={'error': True, 'message': f'Invalid JSON response: {str(e)}'}
            )
            return
        agent.send_output(
            agent_output_name='dnd_api_response',
            agent_result=response_json
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='dnd_api_response',
            agent_result={'error': True, 'message': f'Agent error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='DnDApiNodeBridge')
    run(agent=agent)

if __name__ == '__main__':
    main()
