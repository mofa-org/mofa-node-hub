from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Dummy input for dataflow compatibility
    user_input = agent.receive_parameter('user_input')
    
    dns_results = None
    ping_results = None
    try:
        # DNS Lookup from Multiple Locations
        dns_response = requests.get('https://geonet.shodan.io/api/geodns/yahoo.com', timeout=10)
        dns_response.raise_for_status()
        try:
            dns_results = dns_response.json()
        except Exception:
            dns_results = dns_response.text
    except Exception as e:
        dns_results = {'error': str(e)}
    
    try:
        # Ping from Multiple Locations
        ping_response = requests.get('https://geonet.shodan.io/api/geoping/yahoo.com', timeout=10)
        ping_response.raise_for_status()
        try:
            ping_results = ping_response.json()
        except Exception:
            ping_results = ping_response.text
    except Exception as e:
        ping_results = {'error': str(e)}

    # Output should be serializable and match output port names
    agent.send_output(
        agent_output_name='dns_lookup_result',
        agent_result=dns_results
    )
    agent.send_output(
        agent_output_name='ping_result',
        agent_result=ping_results
    )

def main():
    agent = MofaAgent(agent_name='GeonetApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Ports:
- Receives: user_input (string, dummy input for workflow compatibility)
- Sends: dns_lookup_result (DNS lookup data or error)
         ping_result (Ping data or error)
"""