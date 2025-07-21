# Dependencies: requests
# Note: Add `requests` to your requirements.txt or environment dependencies

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # This agent does not require input, but for dataflow compatibility:
        user_input = agent.receive_parameter('user_input')
        
        # Define the endpoints
        endpoints = [
            "https://postali.app/codigo-postal/65936.json",
            "https://postali.app/codigo-postal/23420.json"
        ]
        results = []
        for url in endpoints:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                # Validate JSON serialization
                data = response.json()
                results.append({"url": url, "result": data})
            except Exception as e:
                results.append({"url": url, "error": str(e)})
        # Output must be serializable
        agent.send_output(
            agent_output_name='postal_info_results',
            agent_result=results
        )
    except Exception as global_error:
        # Send error description in an output-compliant format
        agent.send_output(
            agent_output_name='postal_info_results',
            agent_result={"error": str(global_error)}
        )

def main():
    agent = MofaAgent(agent_name='MexicanPostalApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
