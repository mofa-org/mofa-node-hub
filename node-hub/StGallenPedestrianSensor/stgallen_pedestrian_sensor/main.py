from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate calling by other nodes: receive a user_input parameter (not used)
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://daten.stadt.sg.ch/api/explore/v2.1/catalog/datasets/fussganger-stgaller-innenstadt-vadianstrasse/records?order_by=datum_tag%20DESC&limit=20"
    try:
        # Make the GET request to the provided endpoint
        response = requests.get(endpoint, timeout=20)
        response.raise_for_status()
        # Try to parse JSON, otherwise fallback to text
        try:
            data = response.json()
        except Exception:
            data = response.text
        # Ensure output is serializable
        agent.send_output(
            agent_output_name='pedestrian_data',
            agent_result=data
        )
    except Exception as e:
        # Send error message as output
        agent.send_output(
            agent_output_name='pedestrian_data',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='StGallenPedestrianSensor')
    run(agent=agent)

if __name__ == '__main__':
    main()
