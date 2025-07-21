from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Input required for dataflow compatibility
    user_input = agent.receive_parameter('user_input')
    
    endpoints = {
        'nobel_prizes': 'http://api.nobelprize.org/2.1/nobelPrizes?sort=asc',
        'laureates': 'http://api.nobelprize.org/2.1/laureates?sort=asc'
    }
    results = {}
    
    for key, url in endpoints.items():
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            # Only the topmost 10 entries for response brevity.
            data = response.json()
            # Defensive: convert any non-dict/list JSON to string simply
            if not isinstance(data, (dict, list)):
                data = str(data)
            results[key] = data if isinstance(data, (dict, list)) else str(data)
        except Exception as e:
            results[key] = {'error': f'Failed request for {key}: {str(e)}'}

    agent.send_output(
        agent_output_name='nobel_api_results',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='NobelPrizeInfoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
