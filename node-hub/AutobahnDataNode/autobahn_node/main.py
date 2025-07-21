from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# No external env config required as per agent config
# Requirements: requests

def fetch_data_from_endpoint(endpoint_url):
    try:
        response = requests.get(endpoint_url, timeout=10)
        response.raise_for_status()
        data = response.json()  # API always returns JSON
        return data, None
    except Exception as e:
        return None, str(e)

@run_agent
def run(agent: MofaAgent):
    # Facilitate dataflow, even if no input is required
    user_input = agent.receive_parameter('user_input')
    
    # Autobahn endpoints
    endpoints = {
        'electric_charging_station': 'https://verkehr.autobahn.de/o/autobahn/A1/services/electric_charging_station',
        'roadworks': 'https://verkehr.autobahn.de/o/autobahn/A1/services/roadworks',
        'all_autobahn': 'https://verkehr.autobahn.de/o/autobahn/'
    }

    outputs = {}
    errors = {}
    
    for key, url in endpoints.items():
        result, err = fetch_data_from_endpoint(url)
        if err:
            errors[key] = err
            outputs[key] = None
        else:
            outputs[key] = result

    agent.send_output(
        agent_output_name='autobahn_data',
        agent_result={'data': outputs, 'errors': errors}  # Always serializable
    )

def main():
    agent = MofaAgent(agent_name='AutobahnDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
