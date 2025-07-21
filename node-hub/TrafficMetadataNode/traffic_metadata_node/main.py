from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate compatibility with dataflow requirements
    user_input = agent.receive_parameter('user_input')
    url = "https://www.data.act.gov.au/api/views/s4g9-ndv2/rows.json"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        # Ensure output is serializable
        agent.send_output(
            agent_output_name='traffic_metadata',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='traffic_metadata',
            agent_result={"error": True, "message": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='TrafficMetadataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
