from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests
# Documentation: https://amiiboapi.com/docs/?ref=freepublicapis.com

@run_agent
def run(agent: MofaAgent):
    # Facilitate calls from other nodes even if not used directly
    user_input = agent.receive_parameter('user_input')

    # Try to dynamically get character name if another node provides it
    try:
        params = agent.receive_parameters(['name'])
        character_name = params.get('name', 'mario')  # fallback default
    except Exception:
        character_name = 'mario'  # default as per config

    endpoint = "https://www.amiiboapi.com/api/amiibo/"
    timeout = 10
    try:
        response = requests.get(endpoint, params={'name': character_name}, timeout=timeout)
        response.raise_for_status()
        amiibo_data = response.json()
    except Exception as e:
        amiibo_data = {'error': True, 'message': str(e)}

    # Explicit serialization (dict is acceptable)
    agent.send_output(
        agent_output_name='amiibo_character_info',
        agent_result=amiibo_data
    )

def main():
    agent = MofaAgent(agent_name='AmiiboCharacterNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
