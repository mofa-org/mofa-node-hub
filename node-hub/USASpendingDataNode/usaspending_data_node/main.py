from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate dataflow from other nodes, even though no input is required, we accept a dummy input
    user_input = agent.receive_parameter('user_input')
    API_ENDPOINT = "https://api.usaspending.gov//api/v2/references/toptier_agencies/"
    try:
        response = requests.get(API_ENDPOINT, timeout=30)
        response.raise_for_status()
        # The API returns JSON, which is serializable
        data = response.json()
        # Output the data to the dataflow 'usaspending_data' port
        agent.send_output(
            agent_output_name='usaspending_data',
            agent_result=data
        )
    except Exception as e:
        # Handle all errors and output error details as string
        agent.send_output(
            agent_output_name='usaspending_data',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='USASpendingDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
