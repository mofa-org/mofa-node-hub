from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this node
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://coffee.alexflipnote.dev/random.json', timeout=10)
        response.raise_for_status()
        coffee_data = response.json()
        # Ensure output is serializable
        agent.send_output(
            agent_output_name='coffee_image_json',
            agent_result=coffee_data
        )
    except Exception as e:
        error_msg = {'error': str(e)}
        agent.send_output(
            agent_output_name='coffee_image_json',
            agent_result=error_msg
        )

def main():
    agent = MofaAgent(agent_name='CoffeeImageNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# requests
# (Add to requirements.txt: requests)
