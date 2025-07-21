from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests
# Documentation: https://www.givefood.org.uk/api/?ref=freepublicapis.com

API_BASE_URL = "https://www.givefood.org.uk/api/2"
TIMEOUT = 30  # seconds


def search_foodbanks_by_address(address: str):
    try:
        url = f"{API_BASE_URL}/locations/search/"
        params = {"address": address}
        response = requests.get(url, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {"error": True, "message": str(e)}


def list_foodbank_organisations():
    try:
        url = f"{API_BASE_URL}/foodbanks/"
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {"error": True, "message": str(e)}


@run_agent
def run(agent: MofaAgent):
    """
    Input:
        'action'   : 'search' or 'list' (determines which endpoint to query)
        'address'  : postcode/address IF action=='search' (required for search)
    Output is sent via 'foodbank_output'.
    """
    try:
        # Accept both parameters for maximum flexibility (both as str)
        params = agent.receive_parameters(['action', 'address'])
        action = (params.get('action') or '').strip().lower()
        address = (params.get('address') or '').strip()

        if action == 'search':
            if not address:
                agent.send_output(
                    agent_output_name='foodbank_output',
                    agent_result={'error': True, 'message': 'Missing address parameter for search.'}
                )
                return
            result = search_foodbanks_by_address(address)
        elif action == 'list':
            result = list_foodbank_organisations()
        else:
            result = {'error': True, 'message': "Invalid 'action' parameter. Use 'search' or 'list'."}

        agent.send_output(
            agent_output_name='foodbank_output',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='foodbank_output',
            agent_result={'error': True, 'message': f'Unhandled error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='FoodBankApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
