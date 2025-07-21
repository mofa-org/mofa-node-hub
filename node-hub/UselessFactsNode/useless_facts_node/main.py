# Dependencies:
#   - requests (install via `pip install requests`)
#
# Dataflow ports:
#   - Input: 'fact_type' (string; values: 'random', 'today', 'random_de')
#   - Output: 'useless_fact' (dictionary with keys ['text','source','language'])

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        fact_type = agent.receive_parameter('fact_type')
        
        # Map fact_type to API endpoint
        if fact_type == 'random':
            url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
        elif fact_type == 'today':
            url = 'https://uselessfacts.jsph.pl/api/v2/facts/today'
        elif fact_type == 'random_de':
            url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?language=de'
        else:
            agent.send_output(
                agent_output_name='useless_fact',
                agent_result={'error': f"Invalid fact_type: {fact_type}"}
            )
            return
        
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            output = {
                'text': data.get('text',''),
                'source': data.get('source',''),
                'language': data.get('language','')
            }
            agent.send_output(
                agent_output_name='useless_fact',
                agent_result=output
            )
        else:
            agent.send_output(
                agent_output_name='useless_fact',
                agent_result={'error': f"HTTP {response.status_code}: {response.text}"}
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='useless_fact',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='UselessFactsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
