# Dependencies:
#   requests: ^2.31.0
#   python-dotenv: ^1.0.1 (optional for .env.secret if expanded)
#
# This agent fetches public data from Hacker News for stories, jobs, and comments.
# All inputs/outputs use strict dora-rs interface compliance and serialization guarantees.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

HACKERNEWS_ENDPOINTS = [
    {
        'name': 'story',
        'url': 'https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty',
        'description': 'Provides public Hacker News data in near real time. Includes information on stories.'
    },
    {
        'name': 'job',
        'url': 'https://hacker-news.firebaseio.com/v0/item/192327.json?print=pretty',
        'description': 'Provides public Hacker News data in near real time. Includes information on jobs.'
    },
    {
        'name': 'comment',
        'url': 'https://hacker-news.firebaseio.com/v0/item/2921983.json?print=pretty',
        'description': 'Provides public Hacker News data in near real time. Includes information on comments.'
    },
]

def fetch_hackernews_item(url: str, timeout: int = 30):
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {'error': str(e)}

@run_agent
def run(agent: MofaAgent):
    # No required input, but to facilitate framework node chaining:
    user_input = agent.receive_parameter('user_input')  # Could be ignored; for node-link compliance
    
    output_data = {}
    for item in HACKERNEWS_ENDPOINTS:
        data = fetch_hackernews_item(item['url'])
        # Guarantee serialization (dict)
        output_data[item['name']] = {
            'description': item['description'],
            'data': data
        }
    agent.send_output(
        agent_output_name='hackernews_data',
        agent_result=output_data   # Dict, guaranteed serializable
    )

def main():
    agent = MofaAgent(agent_name='HackerNewsDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
