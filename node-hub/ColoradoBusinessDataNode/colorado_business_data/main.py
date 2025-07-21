from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Fetches all Colorado business records from the public API and outputs as a JSON-serializable Python list. Handles all errors internally to maintain agent boundaries.
    """
    # For dataflow node compliance, accept a dummy string input
'to facilitate downstream connectivity.
    user_input = agent.receive_parameter('user_input')  # Not used, but required per spec

    endpoint = "https://data.colorado.gov/resource/4ykn-tg5h.json"
    try:
        response = requests.get(endpoint, timeout=20)
        response.raise_for_status()
        # The API returns JSON
        data = response.json()  # list/dict
        # Ensure serialization
        agent.send_output(
            agent_output_name='business_data',
            agent_result=data
        )
    except Exception as e:
        # Handle and report error in the output
        agent.send_output(
            agent_output_name='business_data',
            agent_result={
                "error": True,
                "message": str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='ColoradoBusinessDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
