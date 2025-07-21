from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive input parameter (to facilitate dataflow, even if not used)
    user_input = agent.receive_parameter('user_input')
    try:
        api_url = 'https://www.freetogame.com/api/games?platform=pc'
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # Ensure response can be serialized; response.json() usually returns dict/list
        games_data = response.json()
        agent.send_output(
            agent_output_name='games_list',
            agent_result=games_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='games_list',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='FreeGamesDatabaseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# This agent queries the Free-To-Play Games Database API for free PC games. No additional parameters required.
# Output port: 'games_list' (returns list of games or error info)