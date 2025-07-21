# Dependencies:
#   - requests
# 
# To use this agent, ensure `requests` is included in your agent environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # This agent does not require explicit input but keeps port for future compatibility
    user_input = agent.receive_parameter('user_input')
    
    endpoints = {
        'list_characters': 'https://finalspaceapi.com/api/v0/character',
        'character_1': 'https://finalspaceapi.com/api/v0/character/1',
        'all_endpoints': 'https://finalspaceapi.com/api/v0/'
    }

    results = {}
    errors = {}
    
    # Fetch all endpoints with error handling
    for key, url in endpoints.items():
        try:
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            # Try to parse as JSON, fallback to text
            try:
                results[key] = response.json()
            except ValueError:
                results[key] = response.text
        except Exception as e:
            errors[key] = str(e)

    # Send outputs
    agent.send_output(
        agent_output_name='final_space_data',
        agent_result={
            'data': results,
            'errors': errors
        }
    )

def main():
    agent = MofaAgent(agent_name='FinalSpaceAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()
