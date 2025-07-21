from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate connection for potential upstream input, even if unused
    user_input = agent.receive_parameter('user_input')
    try:
        # Endpoint for random cat image in JSON format
        response = requests.get("https://cataas.com/cat?json=true", timeout=10)
        response.raise_for_status()
        data = response.json()
        # Validate serialization
        if not isinstance(data, dict):
            raise ValueError('API response is not a valid dictionary.')
        # Output to framework port
        agent.send_output(
            agent_output_name='cat_image_json',
            agent_result=data
        )
    except Exception as e:
        # Handle and serialize errors
        agent.send_output(
            agent_output_name='cat_image_json',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CatImageApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests (pip install requests)
# Documentation: https://cataas.com/?ref=freepublicapis.com
