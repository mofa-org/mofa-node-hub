from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate possible connection with other nodes, receive placeholder input
    user_input = agent.receive_parameter('user_input')
    
    base_url = "https://www.moogleapi.com/api/v1"
    endpoints = {
        'games': '/games',
        'monsters': '/monsters',
        'characters': '/characters',
    }
    results = {}
    
    try:
        for key, path in endpoints.items():
            url = f"{base_url}{path}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            # Each response is expected to be JSON-decodable
            results[key] = response.json()
    except Exception as e:
        results = {'error': str(e)}
    # Ensure results (even on error) can be serialized
    agent.send_output(
        agent_output_name='moogle_api_data',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='MoogleApiDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
