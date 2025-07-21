# Dependencies: requests
# Optional: python-dotenv (for .env.secret usage)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    """
    Agent to fetch Berufliche Grundbildung records from Swiss public API data.tg.ch.
    If called by another node, expects 'user_input' param to satisfy input format.
    """
    try:
        user_input = agent.receive_parameter('user_input')  # Facilitate framework chaining (even if unused)
        # The agent supports two operations:
        # 1. Fetch all with limit=100
        # 2. Fetch recent records (order_by=jahr DESC, limit=20)
        # Accept 'mode' (either 'all' or 'recent') as string param
        # Default (if no mode): fetch 'all'
        mode = agent.receive_parameter('mode') if 'mode' in agent.input_ports else 'all'
        # Convert mode to string (in case it comes as other type)
        mode = str(mode).lower()
        if mode == 'recent':
            url = 'https://data.tg.ch/api/explore/v2.1/catalog/datasets/dek-abb-1/records?order_by=jahr%20DESC&limit=20'
        else:
            url = 'https://data.tg.ch/api/explore/v2.1/catalog/datasets/dek-abb-1/records?limit=100'
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        # Ensure output serialization
        agent.send_output(
            agent_output_name='records',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='records',
            agent_result={'error': True, 'message': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BeruflicheAbschluesseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
