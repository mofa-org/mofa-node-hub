from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate calls from other nodes, even though this is a fixed endpoint agent
    user_input = agent.receive_parameter('user_input')
    
    endpoints = {
        'ch': 'https://api.zippopotam.us/ch/3007',
        'us': 'https://api.zippopotam.us/us/90210',
    }
    results = {}
    for country_code, url in endpoints.items():
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            json_data = response.json()
            results[country_code] = json_data
        except Exception as e:
            results[country_code] = {'error': str(e)}
    agent.send_output(
        agent_output_name='postal_location_outputs',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='PostalLocationLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
