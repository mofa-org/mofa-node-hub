# Dependencies: requests
# Ensure `requests` package is available in your agent's environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

MOCK_API_MAP = {
    'products': 'https://api.mockae.com/fakeapi/products',
    'coupons': 'https://api.mockae.com/fakeapi/coupons',
    'carts': 'https://api.mockae.com/fakeapi/carts',
    'users': 'https://api.mockae.com/fakeapi/users',
}

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate other nodes to call this node
        user_input = agent.receive_parameter('user_input')  # can be path string ("products", "coupons", etc.)
        endpoint_key = str(user_input).strip().lower()
        
        if endpoint_key not in MOCK_API_MAP:
            agent.send_output(
                agent_output_name='api_result',
                agent_result={
                    'error': True,
                    'message': f'Invalid endpoint key: {endpoint_key}. Must be one of: {list(MOCK_API_MAP.keys())}'
                }
            )
            return
        
        # Make GET request to selected endpoint
        api_url = MOCK_API_MAP[endpoint_key]
        resp = requests.get(api_url, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        agent.send_output(
            agent_output_name='api_result',
            agent_result=result  # Must be serializable (dict/list/str)
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_result',
            agent_result={'error': True, 'message': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='MockApiNodeIntegrator')
    run(agent=agent)

if __name__ == '__main__':
    main()
