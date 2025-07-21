from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this node
    user_input = agent.receive_parameter('user_input')
    
    results = {}
    
    try:
        btc_resp = requests.get('https://api.coinpaprika.com/v1/coins/btc-bitcoin', timeout=15)
        btc_resp.raise_for_status()
        results['bitcoin_info'] = btc_resp.json()
    except Exception as e:
        results['bitcoin_info'] = {'error': str(e)}
    
    try:
        tags_resp = requests.get('https://api.coinpaprika.com/v1/tags', timeout=15)
        tags_resp.raise_for_status()
        results['tags'] = tags_resp.json()
    except Exception as e:
        results['tags'] = {'error': str(e)}
    
    agent.send_output(
        agent_output_name='coinpaprika_output',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='CoinpaprikaNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()