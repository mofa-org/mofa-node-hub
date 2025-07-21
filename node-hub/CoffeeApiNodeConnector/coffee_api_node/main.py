from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call even if no input needed (per requirements)
    user_input = agent.receive_parameter('user_input')  # Not used, but required for interface compliance

    # List of public coffee endpoints
    endpoints = [
        "https://api.sampleapis.com/coffee/hot",
        "https://api.sampleapis.com/coffee/iced"
    ]
    output_results = {}
    for url in endpoints:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            # Validate serializability
            try:
                data = response.json()
            except Exception as e:
                data = response.text
            output_results[url] = data
        except Exception as error:
            output_results[url] = {
                'error': True,
                'message': str(error)
            }
    # Send outputs as a single dictionary keyed by url
    agent.send_output(
        agent_output_name='coffee_api_data',
        agent_result=output_results
    )

def main():
    agent = MofaAgent(agent_name='CoffeeApiNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()