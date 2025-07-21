# Dependencies: requests
# Ensure to include `requests` in your environment (pip install requests)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No input required, but receive dummy user input for compatibility
    user_input = agent.receive_parameter('user_input')
    try:
        # Fetch planets data
        planets_response = requests.get('https://dragonball-api.com/api/planets', timeout=10)
        planets_response.raise_for_status()
        planets_data = planets_response.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='planets_output',
            agent_result={"error": f"Failed to fetch planets data: {str(e)}"}
        )
        planets_data = None
    try:
        # Fetch characters data
        characters_response = requests.get('https://dragonball-api.com/api/characters', timeout=10)
        characters_response.raise_for_status()
        characters_data = characters_response.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='characters_output',
            agent_result={"error": f"Failed to fetch characters data: {str(e)}"}
        )
        characters_data = None

    # Send successful outputs only if data was fetched
    if planets_data is not None:
        agent.send_output(
            agent_output_name='planets_output',
            agent_result=planets_data
        )
    if characters_data is not None:
        agent.send_output(
            agent_output_name='characters_output',
            agent_result=characters_data
        )

def main():
    agent = MofaAgent(agent_name='DragonBallUniverseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
