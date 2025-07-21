from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
#   - requests
#
# API Docs: https://represent.opennorth.ca/api/?ref=freepublicapis.com
#
# Environment: No usage of env vars for this agent.
#
# Input Ports:
#   - first_name: e.g. 'Jack' (string)
#   - postcode: e.g. 'L5G4L3' (string)
# Output Ports:
#   - representatives_by_name (dict): List of representatives data by first name
#   - representatives_by_postcode (dict): List of representatives data by postal code

API_BASE_URL = "https://represent.opennorth.ca/"

@run_agent
def run(agent: MofaAgent):
    try:
        # Try first to receive both possible parameters
        params = agent.receive_parameters(['first_name', 'postcode'])
        first_name = params.get('first_name', '').strip()
        postcode = params.get('postcode', '').strip()
        
        if first_name:
            # Call API to get by first name
            url = f"{API_BASE_URL}representatives/"
            response = requests.get(url, params={"first_name": first_name})
            response.raise_for_status()
            result = response.json()
            agent.send_output(
                agent_output_name='representatives_by_name',
                agent_result=result
            )
            return
        elif postcode:
            url = f"{API_BASE_URL}postcodes/{postcode}/"
            response = requests.get(url)
            response.raise_for_status()
            result = response.json()
            agent.send_output(
                agent_output_name='representatives_by_postcode',
                agent_result=result
            )
            return
        else:
            # Facilitate call from upstream even if no input is present
            user_input = agent.receive_parameter('user_input')  # for graph compatibility
            agent.send_output(
                agent_output_name='representatives_by_postcode',
                agent_result={'error': 'No valid parameters (first_name or postcode) were provided.'}
            )
    except Exception as e:
        # Always safely serialize error
        agent.send_output(
            agent_output_name='representatives_by_postcode',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='OpenNorthRepresentativesNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
