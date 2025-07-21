from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it (no required user input)
    user_input = agent.receive_parameter('user_input')

    TLE_API_ENDPOINT = "https://tle.ivanstanojevic.me/api/tle/25544"
    TIMEOUT = 10  # seconds (configurable)
    
    try:
        response = requests.get(TLE_API_ENDPOINT, timeout=TIMEOUT)
        response.raise_for_status()
        tle_data = response.json()  # Ensure serialization compatibility
    except Exception as e:
        tle_data = {
            "error": True,
            "message": f"Error fetching TLE data: {str(e)}"
        }
    agent.send_output(
        agent_output_name='tle_data',
        agent_result=tle_data  # dict, serializable
    )

def main():
    agent = MofaAgent(agent_name='SatelliteTLETrackerNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
