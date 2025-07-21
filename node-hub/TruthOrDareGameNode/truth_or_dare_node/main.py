from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

def fetch_api(endpoint_url):
    try:
        response = requests.get(endpoint_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {'error': str(e)}

API_OPTIONS = {
    'truth': 'https://api.truthordarebot.xyz/v1/truth',
    'dare': 'https://api.truthordarebot.xyz/api/dare',
    'nhie': 'https://api.truthordarebot.xyz/api/nhie',
    'paranoia': 'https://api.truthordarebot.xyz/api/paranoia',
    'wyr': 'https://api.truthordarebot.xyz/api/wyr',
}

@run_agent
def run(agent: MofaAgent):
    # To allow other nodes to call this node even if they don't pass user_input
    user_input = agent.receive_parameter('user_input')
    api_type = user_input.strip().lower() if user_input else ''
    endpoint = API_OPTIONS.get(api_type)
    if endpoint is None:
        agent.send_output(
            agent_output_name='game_api_response',
            agent_result={
                'error': f"Invalid API option '{api_type}'. Valid options: {list(API_OPTIONS.keys())}"
            }
        )
        return
    data = fetch_api(endpoint)
    # Data must be serializable
    agent.send_output(
        agent_output_name='game_api_response',
        agent_result=data
    )

def main():
    agent = MofaAgent(agent_name='TruthOrDareGameNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
