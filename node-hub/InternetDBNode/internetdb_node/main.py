from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependencies:
# - requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate orchestration compatibility, receive a dummy parameter even though no input is required
    user_input = agent.receive_parameter('user_input')
    
    # Agent configuration (populate dynamically or via YAML if needed)
    endpoint = "https://internetdb.shodan.io/1.1.1.1"  # Normally configurable
    timeout = 10
    retries = 3
    
    last_exception = None
    for attempt in range(retries):
        try:
            response = requests.get(endpoint, timeout=timeout)
            response.raise_for_status()
            # Valid response, try to parse as JSON
            try:
                response_data = response.json()
            except Exception as json_exc:
                # If response is not JSON, fallback to raw content
                response_data = response.text
            # Serialization check
            if not isinstance(response_data, (str, dict, list)):
                response_data = str(response_data)
            agent.send_output(
                agent_output_name='internetdb_result',
                agent_result=response_data
            )
            return
        except Exception as exc:
            last_exception = exc
    # All attempts failed -- send error details
    agent.send_output(
        agent_output_name='internetdb_result',
        agent_result={'error': str(last_exception)}
    )

def main():
    agent = MofaAgent(agent_name='InternetDBNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
