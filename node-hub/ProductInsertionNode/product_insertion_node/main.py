from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    Receives product data as a JSON string, inserts product via POST request to API, returns created product response.
    Input: JSON string (product_data)
    Output: JSON dict (product_insertion_result)
    """
    try:
        # Input handling
        product_data_str = agent.receive_parameter('product_data')
        if not product_data_str:
            agent.send_output(
                agent_output_name='product_insertion_result',
                agent_result={'error': 'Missing product_data input'}
            )
            return
        try:
            product_data = json.loads(product_data_str)
        except Exception as e:
            agent.send_output(
                agent_output_name='product_insertion_result',
                agent_result={'error': f'Invalid JSON: {str(e)}'}
            )
            return

        endpoint = "https://api.predic8.de/shop/v2/products/"
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(endpoint, headers=headers, json=product_data, timeout=10)
        except Exception as e:
            agent.send_output(
                agent_output_name='product_insertion_result',
                agent_result={'error': f'Request error: {str(e)}'}
            )
            return

        try:
            resp_json = response.json()
        except Exception:
            resp_json = {'raw_response': response.text}

        result = {
            'status_code': response.status_code,
            'response': resp_json
        }
        agent.send_output(
            agent_output_name='product_insertion_result',
            agent_result=result
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='product_insertion_result',
            agent_result={'error': f'Unhandled agent exception: {str(ex)}'}
        )

def main():
    agent = MofaAgent(agent_name='ProductInsertionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# To install: pip install requests
