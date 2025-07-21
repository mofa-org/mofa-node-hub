# Dependencies: requests
# No input required, but supports 'user_input' for dataflow compliance.
# Output port name: 'music_api_response'

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Stateless dataflow requirement
    user_input = agent.receive_parameter('user_input')
    # Both endpoints info
    endpoints = [
        {
            "url": "https://openwhyd.org/adrien?format=json",
            "description": "Get the last 20 Tracks of Adrien"
        },
        {
            "url": "https://openwhyd.github.io/openwhyd/API?ref=freepublicapis.com",
            "description": "YouTube Music"
        }
    ]
    results = []
    for endpoint in endpoints:
        try:
            resp = requests.get(endpoint['url'], timeout=10)
            resp.raise_for_status()
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            results.append({
                'description': endpoint['description'],
                'data': data
            })
        except Exception as e:
            results.append({
                'description': endpoint['description'],
                'error': str(e)
            })

    # Ensure serialization (list of dicts)
    agent.send_output(
        agent_output_name='music_api_response',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='OpenWhydMusicNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
