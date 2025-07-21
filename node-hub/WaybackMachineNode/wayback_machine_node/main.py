from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    # Facilitate input from other nodes even if not strictly needed
    user_input = agent.receive_parameter('user_input')
    try:
        # Endpoint is fixed for this agent (as per node code), so no dynamic parameter used
        endpoint = "http://archive.org/wayback/available?url=apple.com"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()  # raise for HTTP errors
        data = response.json()
        # Serialize data for output
        agent.send_output(
            agent_output_name='wayback_snapshot',
            agent_result=data
        )
    except Exception as e:
        # Full error containment and serialization
        agent.send_output(
            agent_output_name='wayback_snapshot',
            agent_result={"error": True, "message": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='WaybackMachineNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
