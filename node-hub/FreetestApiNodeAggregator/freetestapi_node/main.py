from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies: requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate upstream node calls even if ignored
    user_input = agent.receive_parameter('user_input')
    endpoints = [
        "https://freetestapi.com/api/v1/airlines",
        "https://freetestapi.com/api/v1/todos",
        "https://freetestapi.com/api/v1/books"
    ]
    all_results = {}
    try:
        for url in endpoints:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                # Try to parse JSON, fallback to raw text
                try:
                    result = response.json()
                except Exception:
                    result = response.text
                all_results[url] = result
            except Exception as e:
                all_results[url] = {'error': str(e)}
    except Exception as e:
        # Output global fatal error
        agent.send_output(
            agent_output_name='api_aggregate_result',
            agent_result={"error": f"Critical agent failure: {str(e)}"}
        )
        return
    agent.send_output(
        agent_output_name='api_aggregate_result',
        agent_result=all_results
    )

def main():
    agent = MofaAgent(agent_name='FreetestApiNodeAggregator')
    run(agent=agent)

if __name__ == '__main__':
    main()
