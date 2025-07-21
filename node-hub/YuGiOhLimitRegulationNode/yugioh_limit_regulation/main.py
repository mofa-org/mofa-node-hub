from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests
# Make sure 'requests' is added to your requirements.txt / dependencies list.
#
# Stateless agent for fetching current Yu-Gi-Oh! Forbidden & Limited Lists across various formats.

ENDPOINTS = {
    "tcg": "https://dawnbrandbots.github.io/yaml-yugi-limit-regulation/tcg/current.vector.json",
    "rush": "https://dawnbrandbots.github.io/yaml-yugi-limit-regulation/rush/current.vector.json",
    "ocg_ae": "https://dawnbrandbots.github.io/yaml-yugi-limit-regulation/ocg-ae/current.vector.json",
    "ocg": "https://dawnbrandbots.github.io/yaml-yugi-limit-regulation/ocg/current.vector.json",
    "master_duel": "https://dawnbrandbots.github.io/yaml-yugi-limit-regulation/master-duel/current.vector.json",
    "ocg_cn": "https://dawnbrandbots.github.io/yaml-yugi-limit-regulation/ocg-cn/current.vector.json"
}

@run_agent
def run(agent: MofaAgent):
    # input: region string (e.g. 'tcg', 'rush', 'ocg', 'ocg_ae', 'master_duel', 'ocg_cn')
    region = agent.receive_parameter('region')
    
    try:
        region_key = str(region).lower().replace('-', '_')
        if region_key not in ENDPOINTS:
            agent.send_output(
                agent_output_name='forbidden_list',
                agent_result={
                    'error': f"Invalid region key: {region}. Allowed: {list(ENDPOINTS.keys())}"
                }
            )
            return
            
        url = ENDPOINTS[region_key]
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # Attempt to parse json
        data = response.json()
        agent.send_output(
            agent_output_name='forbidden_list',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='forbidden_list',
            agent_result={
                'error': f"Failed to fetch or parse list: {str(e)}"
            }
        )

def main():
    agent = MofaAgent(agent_name='YuGiOhLimitRegulationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
