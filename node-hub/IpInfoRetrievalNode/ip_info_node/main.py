# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Accepts user input (not strictly needed, but for compatibility with dora-rs framework nodes expecting input ports)
    user_input = agent.receive_parameter('user_input')  # will be None or ignored
    
    try:
        endpoints = [
            "https://apip.cc/api-json/8.8.8.8",    # Example: get details for specific IP
            "https://apip.cc/api-json/vk.com",     # Example: get domain IP info
            "https://apip.cc/json"                 # Get own IP and currency
        ]
        results = {}
        for url in endpoints:
            try:
                response = requests.get(url, timeout=8)
                response.raise_for_status()
                # Check if JSON, then load
                data = response.json()
                results[url] = data
            except Exception as e:
                results[url] = {"error": str(e)}
        agent.send_output(
            agent_output_name='ip_info_results',
            agent_result=results
        )
    except Exception as err:
        agent.send_output(
            agent_output_name='ip_info_results',
            agent_result={"error": str(err)}
        )

def main():
    agent = MofaAgent(agent_name='IpInfoRetrievalNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
