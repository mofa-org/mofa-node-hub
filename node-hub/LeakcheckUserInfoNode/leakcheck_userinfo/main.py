from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive required email parameter from the dataflow
        email = agent.receive_parameter('email')
        if not isinstance(email, str) or not email:
            raise ValueError('Input parameter "email" must be a non-empty string.')

        # Form the API endpoint
        api_url = f"https://leakcheck.net/api/public?check={email}"

        # Perform GET request to Leakcheck API
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        try:
            response_data = response.json()
        except Exception:
            response_data = {'raw': response.text}

        # Output the results
        agent.send_output(
            agent_output_name='leakcheck_result',
            agent_result=response_data
        )
    except Exception as e:
        # Return any errors in a controlled, serializable manner
        agent.send_output(
            agent_output_name='leakcheck_result',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='LeakcheckUserInfoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependency: requests
# To install: pip install requests
