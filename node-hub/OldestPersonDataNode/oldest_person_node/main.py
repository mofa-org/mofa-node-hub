# Dependencies: requests (pure standard library fallback below)
# If using outside sandboxed dora-rs, ensure requests is in requirements.txt

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import json
try:
    import requests
except ImportError:
    import urllib.request as urllib_request
    import urllib.error as urllib_error
    
    def simple_get(url):
        try:
            with urllib_request.urlopen(url) as response:
                return response.read().decode()
        except urllib_error.URLError as e:
            return json.dumps({'error': str(e)})
else:
    def simple_get(url):
        try:
            resp = requests.get(url,timeout=15)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            return json.dumps({'error': str(e)})

API_ENDPOINTS = {
    'oldest_living': 'https://whoistheoldest.com/api/oldest-living-person',
    'oldest_ever': 'https://whoistheoldest.com/api/oldest-person-ever',
}

def fetch_person_data():
    results = {}
    for key, url in API_ENDPOINTS.items():
        data_raw = simple_get(url)
        try:
            data = json.loads(data_raw)
        except Exception:
            data = {'raw': data_raw}
        results[key] = data
    return results

@run_agent
def run(agent: MofaAgent):
    # Facilitate dataflow, even if unused, for compatibility
    user_input = agent.receive_parameter('user_input')

    try:
        person_data = fetch_person_data()
        agent.send_output(
            agent_output_name='oldest_person_data',
            agent_result=person_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='oldest_person_data',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='OldestPersonDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
