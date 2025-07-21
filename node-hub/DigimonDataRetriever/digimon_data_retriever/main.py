# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # As no input is required, add this line for integration compatibility:
    user_input = agent.receive_parameter('user_input')
    endpoints = [
        'https://digi-api.com/api/v1/digimon/16',
        'https://digi-api.com/api/v1/digimon',
    ]
    results = {}
    try:
        for url in endpoints:
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                # The API returns JSON
                results[url] = resp.json()
            except Exception as e_inner:
                # Error for individual endpoint
                results[url] = {'error': str(e_inner)}
        agent.send_output(
            agent_output_name='digimon_data',
            agent_result=results  # dict is serializable
        )
    except Exception as e:
        # Total error scenario
        agent.send_output(
            agent_output_name='digimon_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='DigimonDataRetriever')
    run(agent=agent)

if __name__ == '__main__':
    main()
