from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes calling this agent in a dataflow pipeline
    user_input = agent.receive_parameter('user_input')
    try:
        # API configuration (hardcoded as per config and documented API)
        base_url = "https://ssd-api.jpl.nasa.gov/cad.api"
        params = {
            "des": "433",
            "date-min": "1900-01-01",
            "date-max": "2100-01-01",
            "dist-max": "0.2"
        }
        response = requests.get(base_url, params=params, timeout=20)
        response.raise_for_status()
        # Try JSON parse, else return as text
        try:
            api_result = response.json()
        except Exception:
            api_result = response.text
        agent.send_output(
            agent_output_name='close_approach_data',
            agent_result=api_result
        )
    except Exception as err:
        # Return error in serializable form
        agent.send_output(
            agent_output_name='close_approach_data',
            agent_result={
                "error": True,
                "message": str(err)
            }
        )

def main():
    agent = MofaAgent(agent_name='JPLOrbitalApproachNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests  # For HTTP GET requests (pip install requests)
'''
