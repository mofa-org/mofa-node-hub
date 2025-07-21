from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate pipeline call even if not required
        user_input = agent.receive_parameter('user_input')
        # Choose which product endpoint to call via input parameter
        params = agent.receive_parameters(['brand', 'product_type'])
        brand = params.get('brand', '').strip().lower()
        product_type = params.get('product_type', '').strip().lower()
        
        # Endpoint mappings
        endpoints = {
            'maybelline': {
                'url': 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline',
                'description': 'Get Makeup from Maybelline'
            },
            'covergirl_lipstick': {
                'url': 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=covergirl&product_type=lipstick',
                'description': 'Get Lipsticks from Covergirl'
            }
        }
        # Endpoint selection logic
        if brand == 'maybelline':
            endpoint_info = endpoints['maybelline']
        elif brand == 'covergirl' and product_type == 'lipstick':
            endpoint_info = endpoints['covergirl_lipstick']
        else:
            agent.send_output(
                agent_output_name='error',
                agent_result='Invalid brand or product_type. Supported: maybelline; or covergirl+lipstick.'
            )
            return

        try:
            resp = requests.get(endpoint_info['url'], timeout=10)
            resp.raise_for_status()
            # The makeup API returns a JSON array - ensure serialization
            try:
                data = resp.json()
                agent.send_output(
                    agent_output_name='products',
                    agent_result=data  # Already serializable (list of dicts)
                )
            except Exception as je:
                agent.send_output(
                    agent_output_name='error',
                    agent_result=f'JSON decode error: {str(je)}'
                )
        except requests.RequestException as re:
            agent.send_output(
                agent_output_name='error',
                agent_result=f'HTTP error: {str(re)}'
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result=f'Agent execution error: {str(e)}'
        )

def main():
    agent = MofaAgent(agent_name='MakeupProductFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# To install: pip install requests
# All inputs/outputs use framework interface. Stateless, errors contained, serialization enforced.