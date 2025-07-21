# Dependencies: requests
# No external secrets required
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

def fetch_radical_character(api_url: str) -> dict:
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception:
            # Fallback if response isn't JSON
            data = {'content': response.text}
        return {'success': True, 'data': data}
    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': str(e)}

@run_agent
def run(agent: MofaAgent):
    # Receives 'user_input' for compatibility, though unused
    user_input = agent.receive_parameter('user_input')

    api_url = "http://ccdb.hemiola.com/characters/radicals/85"
    result = fetch_radical_character(api_url)
    agent.send_output(
        agent_output_name='character_info',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='RadicalCharacterApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
