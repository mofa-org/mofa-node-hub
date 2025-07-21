from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Fetches the newest PlayStation games in Switzerland from the official PlayStation Store API.
    Output is sent as JSON serializable dictionary.
    """
    # Accept an optional 'user_input' to facilitate chain-calling, though input is not required
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://store.playstation.com/store/api/chihiro/00_09_000/container/ch/de/999/STORE-MSF75508-FULLGAMES"
    params = {
        "size": "20",
        "start": "0",
        "sort": "release_date"
    }
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(endpoint, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        # Only output fields that are definitely serializable
        agent.send_output(
            agent_output_name='ps_games_data',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='ps_games_data',
            agent_result={"error": True, "detail": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='PlayStationGamesFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
#
# This agent relies only on built-in libraries and the requests module. Add 'requests' to dependencies.
