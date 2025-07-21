from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate dataflow calls from other nodes
    user_input = agent.receive_parameter('user_input')
    
    endpoints = {
        'ailments': 'https://mhw-db.com/ailments',
        'monsters': 'https://mhw-db.com/monsters',
        'armor': 'https://mhw-db.com/armor',
    }
    results = {}
    
    try:
        for key, url in endpoints.items():
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                # Try to parse JSON, fallback to raw text
                try:
                    results[key] = resp.json()
                except Exception:
                    results[key] = resp.text
            except Exception as e:
                results[key] = {'error': str(e)}
    except Exception as e:
        results = {'critical_error': str(e)}
    
    agent.send_output(
        agent_output_name='mhworld_info',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='MonsterHunterWorldNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
