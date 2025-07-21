from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate compatibility with other nodes (as per requirements)
    user_input = agent.receive_parameter('user_input')

    # Define API endpoints and their descriptions
    endpoints = [
        {
            "name": "skill_cards",
            "url": "https://dawnbrandbots.github.io/yaml-yugi/skill.json",
            "desc": "All Yu-Gi-Oh! TCG Speed Duel Skill Cards"
        },
        {
            "name": "rush_cards",
            "url": "https://dawnbrandbots.github.io/yaml-yugi/rush.json",
            "desc": "All Yu-Gi-Oh! Rush Duel cards"
        }
    ]

    outputs = {}
    errors = {}

    for endpoint in endpoints:
        try:
            response = requests.get(endpoint["url"], timeout=10)
            response.raise_for_status()
            # Confirm that returned content is serializable (json)
            data = response.json()
            outputs[endpoint["name"]] = data
        except Exception as e:
            errors[endpoint["name"]] = str(e)
            outputs[endpoint["name"]] = None

    agent.send_output(
        agent_output_name='yugioh_data',
        agent_result={
            "results": outputs,
            "errors": errors,
        }
    )

def main():
    agent = MofaAgent(agent_name='YuGiOhCardNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# Notes: Requires outbound HTTPS access to GitHub Pages. Outputs full JSON from two public Yu-Gi-Oh! card endpoints. All exceptions trapped and reported via 'errors'.