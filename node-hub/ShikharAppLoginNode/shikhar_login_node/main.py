# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
from requests.exceptions import RequestException

@run_agent
def run(agent: MofaAgent):
    '''
    ShikharAppLoginNode - Agent for Shikhar app login endpoint
    - Endpoint: https://shikhar.hulcd.com/login
    - Method: GET
    - No input parameters required
    '''
    # Facilitate dataflow for future expansion/config
    user_input = agent.receive_parameter('user_input')

    endpoint = "https://shikhar.hulcd.com/login"
    timeout = 30  # seconds
    max_retries = 3
    result = None
    error = None

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(endpoint, timeout=timeout)
            response.raise_for_status()
            # Serialize response as text (response.json possible, but structure is unknown)
            result = response.text
            break
        except RequestException as e:
            error = f"Attempt {attempt} failed: {str(e)}"
            continue
    
    if result:
        agent.send_output(
            agent_output_name='shikhar_login_response',
            agent_result=str(result)
        )
    else:
        agent.send_output(
            agent_output_name='shikhar_login_response',
            agent_result=str({
                "success": False,
                "error": error or "Unknown error encountered during login API call"
            })
        )

def main():
    agent = MofaAgent(agent_name='ShikharAppLoginNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
