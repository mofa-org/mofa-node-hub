from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive user input for the 'check' parameter
    try:
        user_input = agent.receive_parameter('user_input')  # Facilitate other nodes to call it
        check_value = agent.receive_parameter('check')
        if not check_value:
            check_value = user_input  # fallback if only user_input is used
        if not check_value:
            raise ValueError('Missing required input: "check" or "user_input" must be provided.')
        
        endpoint = 'https://leakcheck.net/api/public'
        params = {'check': check_value}

        resp = requests.get(endpoint, params=params, timeout=10)
        try:
            resp.raise_for_status()
        except requests.HTTPError as e:
            agent.send_output(
                agent_output_name='leakcheck_api_error',
                agent_result={'error': f'Request failed with status {resp.status_code}: {str(e)}'}
            )
            return
        
        try:
            data = resp.json()
        except Exception as e:
            # Could not decode JSON
            agent.send_output(
                agent_output_name='leakcheck_api_error',
                agent_result={'error': 'Response content is not valid JSON.', 'content': resp.text}
            )
            return
        
        agent.send_output(
            agent_output_name='leakcheck_api_response',
            agent_result=data if isinstance(data, (dict, list)) else str(data)
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='leakcheck_api_error',
            agent_result={'error': str(ex)}
        )

def main():
    agent = MofaAgent(agent_name='LeakcheckPublicAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests