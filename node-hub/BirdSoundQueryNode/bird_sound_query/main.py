from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive the "query" parameter from upstream
    try:
        user_query = agent.receive_parameter('query')  # String input (e.g. 'troglodytes troglodytes', 'cnt:brazil')
    except Exception as e:
        agent.send_output('error', {'error': f'Error receiving parameter: {str(e)}'})
        return

    # Ensure type string
    if not isinstance(user_query, str):
        try:
            user_query = str(user_query)
        except Exception as e:
            agent.send_output('error', {'error': f'Could not cast input to string: {str(e)}'})
            return
    # Prepare API endpoint
    endpoint = 'https://xeno-canto.org/api/2/recordings'
    params = {'query': user_query}
    try:
        response = requests.get(endpoint, params=params, timeout=15)
        response.raise_for_status()
        api_response = response.json()
    except Exception as e:
        agent.send_output('error', {'error': f'API request failed: {str(e)}'})
        return

    # Output API response (as dict, guaranteed serializable)
    agent.send_output(
        agent_output_name='bird_sounds',
        agent_result=api_response
    )

def main():
    agent = MofaAgent(agent_name='BirdSoundQueryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests (install via pip if needed)
"""
Design notes:
- Input: parameter 'query' (e.g. any valid search: 'troglodytes troglodytes', 'cnt:brazil')
- Output: data on port 'bird_sounds' (dict)
- Error-handling: error strings output on port 'error'
- No state retained
- All types string-checked/converted
- requests required for HTTP GET
- All output is serializable
"""