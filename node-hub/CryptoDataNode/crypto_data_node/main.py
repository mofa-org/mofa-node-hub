from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# No sensitive env vars needed (public API)

@run_agent
def run(agent: MofaAgent):
    """
    CryptoDataNode:
    - get historical price of Bitcoin on a specific date
    - search crypto by keyword query
    Input params:
      - operation: 'get_price' or 'search' (str, required)
      - date (for get_price): format 'dd-mm-yyyy', optional if operation is 'search'
      - query (for search): string, optional if operation is 'get_price'
    Output names:
      - 'api_result': dict with API response or error
    """
    try:
        # Allow flexible operation, params are strings
        param_dict = agent.receive_parameters(['operation', 'date', 'query'])
        operation = param_dict.get('operation', '').strip().lower()

        if operation == 'get_price':
            date_str = param_dict.get('date', '').strip()
            if not date_str:
                agent.send_output(
                    agent_output_name='api_result',
                    agent_result={'error': 'Missing required parameter: date for get_price'}
                )
                return
            url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history'
            params = {'date': date_str}
            try:
                resp = requests.get(url, params=params, timeout=30)
                resp.raise_for_status()
                data = resp.json()
                agent.send_output('api_result', data)
            except Exception as e:
                agent.send_output('api_result', {'error': f'API request failed: {str(e)}'})

        elif operation == 'search':
            query_str = param_dict.get('query', '').strip()
            if not query_str:
                agent.send_output(
                    agent_output_name='api_result',
                    agent_result={'error': 'Missing required parameter: query for search'}
                )
                return
            url = 'https://api.coingecko.com/api/v3/search'
            params = {'query': query_str}
            try:
                resp = requests.get(url, params=params, timeout=30)
                resp.raise_for_status()
                data = resp.json()
                agent.send_output('api_result', data)
            except Exception as e:
                agent.send_output('api_result', {'error': f'API request failed: {str(e)}'})
        else:
            agent.send_output(
                agent_output_name='api_result',
                agent_result={'error': 'Invalid operation. Use "get_price" or "search".'}
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_result',
            agent_result={'error': f'Internal error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='CryptoDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Dataflow Port Info:
- Inputs (via .receive_parameters): 'operation', 'date', 'query' (all str)
- Output: 'api_result' (dict, always serializable)
- Stateless
- All exceptions handled, never crashes
"""