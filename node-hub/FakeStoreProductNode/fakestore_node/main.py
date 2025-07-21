# Dependencies: requests
# To install: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent to interface with FakeStoreAPI for products, categories, and sorted product listings.
    Expected input: action (string)
        Allowed values:
            - 'get_all_products'
            - 'get_product_1'
            - 'get_all_categories'
            - 'get_products_sorted_desc'
    """
    try:
        action = agent.receive_parameter('action')  # string input
        base_url = "https://fakestoreapi.com"
        result = None

        if action == "get_all_products":
            resp = requests.get(f"{base_url}/products", timeout=10)
            resp.raise_for_status()
            result = resp.json()
            out_port = "all_products"
        elif action == "get_product_1":
            resp = requests.get(f"{base_url}/products/1", timeout=10)
            resp.raise_for_status()
            result = resp.json()
            out_port = "product_1"
        elif action == "get_all_categories":
            resp = requests.get(f"{base_url}/products/categories", timeout=10)
            resp.raise_for_status()
            result = resp.json()
            out_port = "all_categories"
        elif action == "get_products_sorted_desc":
            resp = requests.get(f"{base_url}/products", params={"sort": "desc"}, timeout=10)
            resp.raise_for_status()
            result = resp.json()
            out_port = "sorted_products"
        else:
            result = {"error": f"Invalid action: {action}"}
            out_port = "error"
        
        agent.send_output(
            agent_output_name=out_port,
            agent_result=result
        )
    except Exception as e:
        # Output the error as a string (ensure serialization)
        agent.send_output(
            agent_output_name="error",
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='FakeStoreProductNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
