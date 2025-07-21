# Dependencies: requests
# You must install requests via: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent for interfacing with osu.direct public beatmap search and info API.
    - Supported endpoints:
      - /api/v2/search : Beatmap search
      - /api/v2/s/{id} : Get beatmap by ID
    Inputs:
        Required string 'mode' in ['search', 'beatmap', 'set']
        If mode=='beatmap': requires 'id' (beatmap id as string)
        If mode=='set': requires 'id' (set id as string)
        If mode=='search': requires 'params' (search query string, e.g., 'aim')
    Output:
        Data returned by API
    """
    try:
        mode = agent.receive_parameter('mode')  # 'search', 'beatmap', 'set' as string
        mode = str(mode).strip().lower()

        BASE = "https://osu.direct/api/v2"

        if mode == 'search':
            params = agent.receive_parameter('params')  # free-text query (string)
            url = f"{BASE}/search"
            resp = requests.get(url, params={'q': params}, timeout=15)
            resp.raise_for_status()
            output = resp.json()
            agent.send_output('osu_search_result', output)
            return
        elif mode == 'beatmap':
            id_ = agent.receive_parameter('id')  # string beatmap id
            url = f"{BASE}/s/{id_}"
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            output = resp.json()
            agent.send_output('osu_beatmap_result', output)
            return
        elif mode == 'set':
            id_ = agent.receive_parameter('id')  # string beatmap set id
            url = f"{BASE}/s/{id_}"
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            output = resp.json()
            agent.send_output('osu_beatmap_set_result', output)
            return
        else:
            agent.send_output('osu_error', {'error': 'Invalid mode specified. Mode must be one of: search, beatmap, set.'})
            return
    except Exception as e:
        agent.send_output('osu_error', {'error': str(e)})
        return

def main():
    agent = MofaAgent(agent_name='OsuBeatmapSearchNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
