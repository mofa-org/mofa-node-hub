from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os
import json

default_endpoint = "https://apps.fedoraproject.org/datagrepper/v2/search"
default_timeout = 30

@run_agent
def run(agent: MofaAgent):
    """
    FedoraMessageQueryNode
    Queries Fedora Messaging historical messages via the official HTTP API endpoint.
    Inputs (string via dataflow ports):
        - username (optional)
        - package (optional)
        - source (optional)
        - topic (optional)
        - page (optional)
        - rows_per_page (optional)
        - other valid Fedora datagrepper query parameters if desired as string (e.g., 'organization')
    Outputs:
        - results: The API response as a dict (always serializable)
    """
    try:
        # Always receive 'user_input' to support dataflow, even if not used directly.
        user_input = agent.receive_parameter('user_input')
        
        # Accept all possible query inputs as a single data-driven dictionary, expecting strings
        # Example: 'username', 'package', 'source', 'topic', 'page', 'rows_per_page'
        input_params = agent.receive_parameters([
            'username', 'package', 'source', 'topic', 'page', 'rows_per_page'
        ])

        # Remove empty/null parameters (i.e. skip if not provided)
        query_params = {k: v for k, v in input_params.items() if v is not None and str(v).strip() != ''}

        # Optional: parse int types for page/rows_per_page if present (API expects ints)
        for int_key in ['page', 'rows_per_page']:
            if int_key in query_params:
                try:
                    query_params[int_key] = int(query_params[int_key])
                except Exception:
                    # If conversion fails, remove the key so API doesn't break
                    query_params.pop(int_key)

        # Prepare endpoint and timeout
        endpoint = os.environ.get('FEDORA_DG_ENDPOINT', default_endpoint)
        timeout = int(os.environ.get('FEDORA_DG_TIMEOUT', default_timeout))

        # Perform GET request
        response = requests.get(endpoint, params=query_params, timeout=timeout)
        response.raise_for_status()
        try:
            api_result = response.json()
        except Exception:
            api_result = {'error': 'Failed to parse API response as JSON.'}

        # Output must be serializable (dict)
        agent.send_output(
            agent_output_name='results',
            agent_result=api_result
        )
    except Exception as e:
        # Full error handling, output as error record
        agent.send_output(
            agent_output_name='results',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='FedoraMessageQueryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
    - requests
Environment variable support:
    - FEDORA_DG_ENDPOINT (override endpoint)
    - FEDORA_DG_TIMEOUT (override timeout in seconds)
"""