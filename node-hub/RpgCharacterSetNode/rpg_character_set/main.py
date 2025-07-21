# Dependencies: requests
# No API key required

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Even though this node doesn't require input, add placeholder for pipeline consistency
    user_input = agent.receive_parameter('user_input')
    
    character_url = "https://set.world/api/roll/character"
    set_url = "https://set.world/api/roll/set"

    try:
        char_resp = requests.get(character_url, timeout=10)
        set_resp = requests.get(set_url, timeout=10)
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': f'HTTP request failed: {str(e)}'}
        )
        return
    
    if char_resp.status_code != 200 or set_resp.status_code != 200:
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': f'Character ({char_resp.status_code}), Set ({set_resp.status_code})'}
        )
        return

    try:
        char_data = char_resp.json()
        set_data = set_resp.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': f'JSON parse error: {str(e)}'}
        )
        return

    # Output both responses on separate ports for flexibility
    agent.send_output(
        agent_output_name='character',
        agent_result=char_data
    )
    agent.send_output(
        agent_output_name='item_set',
        agent_result=set_data
    )

def main():
    agent = MofaAgent(agent_name='RpgCharacterSetNode')
    run(agent=agent)

if __name__ == '__main__':
    main()