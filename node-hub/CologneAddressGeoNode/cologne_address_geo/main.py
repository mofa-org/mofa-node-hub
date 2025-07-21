# CologneAddressGeoNode
# Dependencies: requests
# Documentation: https://offenedaten-koeln.de/dataset/adressen-köln?ref=freepublicapis.com

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it, even if not strictly needed
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://geoportal.stadt-koeln.de/arcgis/rest/services/basiskarten/adressen_gesamt/MapServer?f=pjson"
    try:
        response = requests.get(endpoint, timeout=15)
        response.raise_for_status()
        # Always send a dict output
        data = response.json()
        agent.send_output(
            agent_output_name='address_geojson',
            agent_result=data
        )
    except Exception as e:
        # Contain all errors and send as output
        agent.send_output(
            agent_output_name='address_geojson',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CologneAddressGeoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
