# Dependencies: requests
# Description: XKCDComicFetcher agent fetches XKCD comic 614 and the latest comic as JSON.
# Documentation: https://xkcd.com/json.html

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # To allow chaining/calling by other nodes
    results = {}
    comics = {
        'comic_614': 'https://xkcd.com/614/info.0.json',
        'current_comic': 'https://xkcd.com/info.0.json'
    }
    for name, url in comics.items():
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            # XKCD returns JSON
            data = resp.json()
            results[name] = data
        except Exception as e:
            results[name] = {'error': str(e)}

    agent.send_output(
        agent_output_name='xkcd_comics',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='XKCDComicFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
