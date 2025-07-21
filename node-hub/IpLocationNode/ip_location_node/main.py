# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitates compatibility with pipeline even if unused
    user_input = agent.receive_parameter('user_input')  # For dataflow chaining
    try:
        # URLs to query
        endpoints = [
            "http://ip-api.com/json/91.231.110.0",
            "http://ip-api.com/json/24.48.0.1"
        ]
        results = []
        for url in endpoints:
            try:
                resp = requests.get(url, timeout=8)
                resp.raise_for_status()
                data = resp.json()  # Make sure response is serializable
            except Exception as e:
                data = {
                    'query_url': url,
                    'error': str(e)
                }
            results.append(data)

        # Output delivery (list of dicts, serializable)
        agent.send_output(
            agent_output_name='ip_location_results',
            agent_result=results
        )
    except Exception as main_err:
        # Contain all top-level errors
        agent.send_output(
            agent_output_name='ip_location_results',
            agent_result=[{'error': str(main_err)}]
        )

def main():
    agent = MofaAgent(agent_name='IpLocationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
