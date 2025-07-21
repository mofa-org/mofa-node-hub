# Dependencies:
# requests (for HTTP requests)
# Add `requests` to requirements.txt or your dependency list.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes' calls, receive an unused parameter
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raises error for bad responses
        try:
            data = response.json()
        except Exception as json_err:
            agent.send_output(
                agent_output_name='error',
                agent_result=f"JSONDecodeError: {str(json_err)}"
            )
            return
        # Sanitize output to ensure serialization (truncate if large)
        if isinstance(data, list) and len(data) > 100:
            data_out = data[:100]  # Only send first 100 entries to avoid overloading outputs
        else:
            data_out = data
        agent.send_output(
            agent_output_name='service_requests',
            agent_result=data_out
        )
    except requests.RequestException as req_err:
        agent.send_output(
            agent_output_name='error',
            agent_result=f"RequestException: {str(req_err)}"
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result=f"UnhandledException: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='NYCServiceRequestNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
