from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it
    user_input = agent.receive_parameter('user_input')
    # This node fetches 5 random "woah" quotes from the API.
    try:
        response = requests.get("https://whoa.onrender.com/whoas/random?results=5", timeout=10)
        response.raise_for_status()
        json_data = response.json()
        # Output should be serializable
        agent.send_output(
            agent_output_name='woah_quotes',
            agent_result=json_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='woah_quotes',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='WhoaQuoteNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
