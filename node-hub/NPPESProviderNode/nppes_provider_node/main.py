from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# Dependencies:
#   - requests

@run_agent
def run(agent: MofaAgent):
    # To allow other nodes to call this node and conform with dora-rs interface,
    # even if code does not require any input, we explicitly receive an input ("user_input")
    user_input = agent.receive_parameter('user_input')
    
    # Configurations (can be moved to environment variables or agent config)
    endpoint = "https://npiregistry.cms.hhs.gov/api/?version=2.1&city=washington"
    request_type = "GET"
    timeout = 15
    
    try:
        if request_type.upper() == "GET":
            response = requests.get(endpoint, timeout=timeout)
        else:
            raise ValueError("Unsupported request_type: only 'GET' is implemented.")
        
        response.raise_for_status()
        # Ensure response is serializable (send dict)
        try:
            result = response.json()
        except Exception as json_err:
            result = {'error': 'Invalid JSON response', 'details': str(json_err)}
    except Exception as err:
        result = {'error': 'Request failed', 'details': str(err)}
    
    agent.send_output(
        agent_output_name='nppes_api_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='NPPESProviderNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
