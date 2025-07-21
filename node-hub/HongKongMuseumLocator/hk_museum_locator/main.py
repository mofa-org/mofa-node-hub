from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Accept a string input to facilitate node-chain compatibility, though it is unused
    user_input = agent.receive_parameter('user_input')
    
    endpoint = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch"
    params = {"q": "museums"}
    headers = {
        'Accept': 'application/json'
    }
    try:
        response = requests.get(endpoint, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        result = response.json()
        # Ensure JSON serializability
        if not isinstance(result, (dict, list)):
            result = {"result": str(result)}
        agent.send_output(
            agent_output_name='museum_locations',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='museum_locations',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='HongKongMuseumLocator')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
#   (Install via: pip install requests)
