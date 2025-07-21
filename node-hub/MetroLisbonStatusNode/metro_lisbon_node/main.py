from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate future input compatibility (required per framework guidelines)
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://app.metrolisboa.pt/status/getLinhas.php"
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Attempt to parse result; fallback to text
        try:
            status_data = response.json()
        except Exception:
            status_data = response.text
        agent.send_output(
            agent_output_name='lines_status',
            agent_result=status_data if isinstance(status_data, (dict, list, str)) else str(status_data)
        )
    except Exception as e:
        # Return error message as output
        agent.send_output(
            agent_output_name='lines_status',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='MetroLisbonStatusNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   requests
#   mofa.agent_build.base.base_agent
