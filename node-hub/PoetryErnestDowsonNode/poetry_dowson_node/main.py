# poetry_dowson_node.py
# Dependencies: requests
# Make sure to add 'requests' to your requirements.txt

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # For dataflow/compatibility: receive 'user_input' (not used)
    user_input = agent.receive_parameter('user_input')
    endpoints = {
        'all_poems': 'https://poetrydb.org/author/Ernest%20Dowson',
        'love_lines': 'https://poetrydb.org/title/love/lines.json'
    }
    results = {}
    try:
        # Query all poems by Dowson
        resp1 = requests.get(endpoints['all_poems'], timeout=10)
        resp1.raise_for_status()
        try:
            results['all_poems'] = resp1.json()
        except Exception as e:
            results['all_poems'] = {'error': f'Error parsing JSON: {e}', 'raw': resp1.text}
        # Query love lines
        resp2 = requests.get(endpoints['love_lines'], timeout=10)
        resp2.raise_for_status()
        try:
            results['love_lines'] = resp2.json()
        except Exception as e:
            results['love_lines'] = {'error': f'Error parsing JSON: {e}', 'raw': resp2.text}
        agent.send_output(
            agent_output_name='poetrydb_results',
            agent_result=results
        )
    except requests.RequestException as e:
        agent.send_output(
            agent_output_name='poetrydb_results',
            agent_result={ 'error': f'Network or request error: {e}' }
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='poetrydb_results',
            agent_result={ 'error': str(e) }
        )

def main():
    agent = MofaAgent(agent_name='PoetryErnestDowsonNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
