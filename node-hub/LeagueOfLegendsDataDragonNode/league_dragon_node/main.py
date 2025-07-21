from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it, even if no input is required.
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Make sure result is serializable (dict)
        result = response.json()
        agent.send_output(
            agent_output_name='league_champion_data',
            agent_result=result
        )
    except Exception as e:
        # Return error message as a string
        agent.send_output(
            agent_output_name='league_champion_data',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='LeagueOfLegendsDataDragonNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
#
# Ensure 'requests' is available in the runtime environment.
# Output delivered via 'league_champion_data' dataflow port as a dict containing champion JSON data or an error message.