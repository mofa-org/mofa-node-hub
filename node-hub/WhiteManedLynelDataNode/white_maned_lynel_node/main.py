from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No required input, but facilitate graph connectivity
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel"
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad status
        data = response.json()  # The data is JSON serializable
    except Exception as e:
        # Error handling: send string error message
        agent.send_output(
            agent_output_name='white_maned_lynel_data',
            agent_result={"error": str(e)}
        )
        return

    agent.send_output(
        agent_output_name='white_maned_lynel_data',
        agent_result=data
    )

def main():
    agent = MofaAgent(agent_name='WhiteManedLynelDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
