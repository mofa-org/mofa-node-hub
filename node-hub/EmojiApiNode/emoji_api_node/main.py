from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os
import json

@run_agent
def run(agent: MofaAgent):
    """
    Sends requests to the EmojiHub API to fetch all emojis, all travel-and-places emojis, or a random emoji based on the 'action' parameter.
    Acceptable actions: 'all', 'travel_and_places', 'random'.
    Optional: provide 'timeout' as integer seconds.
    """
    try:
        params = agent.receive_parameters(['action', 'timeout'])
        action = params.get('action', 'random').strip().lower()
        timeout_s = params.get('timeout', '')
        try:
            timeout = int(timeout_s) if timeout_s else 10
        except Exception:
            timeout = 10
        base_url = "https://emojihub.yurace.pro/api"
        # Select endpoint
        if action == 'all':
            url = f"{base_url}/all"
        elif action == 'travel_and_places':
            url = f"{base_url}/all/category/travel-and-places"
        else:
            url = f"{base_url}/random"
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        result = resp.json()
        agent.send_output(
            agent_output_name='emoji_result',
            agent_result=result
        )
    except Exception as e:
        # Error output as dictionary
        agent.send_output(
            agent_output_name='emoji_result',
            agent_result={"error": True, "message": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='EmojiApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
# DEPENDENCIES:
# - requests
"""