from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # For dataflow consistency; allows chaining by other nodes.
    user_input = agent.receive_parameter('user_input')

    try:
        response = requests.get('https://swapi.dev/api/people/1')
        response.raise_for_status()
        result = response.json()
    except Exception as e:
        # Send error details as string in case of failure
        agent.send_output(
            agent_output_name='character_info',
            agent_result={"error": True, "description": str(e)}
        )
        return

    # Send result (dict is JSON serializable)
    agent.send_output(
        agent_output_name='character_info',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='StarWarsCharacterInfoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
