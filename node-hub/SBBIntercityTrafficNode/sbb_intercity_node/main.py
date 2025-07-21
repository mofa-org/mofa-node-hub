# Dependencies: requests
# Ensure you have requests installed using: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

def fetch_sbb_data(endpoint, params=None):
    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()
        # Limit data size (serialization safety & output compactness)
        return result if isinstance(result, dict) else {'data': result}
    except Exception as e:
        return {'error': str(e)}

@run_agent
def run(agent: MofaAgent):
    # Receive input to select which data to fetch; default to 'departures' for compatibility
    # Optional input: 'data_type' in ['departures', 'cancellations', 'delays']
    data_type = agent.receive_parameter('data_type')
    if not data_type:
        data_type = 'departures'  # default
    data_type = str(data_type).strip().lower()
    
    endpoints = {
        'departures': {
            'endpoint': 'https://data.sbb.ch/api/explore/v2.1/catalog/datasets/ist-daten-sbb/records',
            'params': {
                'limit': '20',
                'refine': 'verkehrsmittel_text:"IC"',
            }
        },
        'cancellations': {
            'endpoint': 'https://data.sbb.ch/api/explore/v2.1/catalog/datasets/ist-daten-sbb/records',
            'params': {
                'limit': '20',
                'refine_1': 'verkehrsmittel_text:"IC"',
                'refine_2': 'faellt_aus_tf:"true"',
            }
        },
        'delays': {
            'endpoint': 'https://data.sbb.ch/api/explore/v2.1/catalog/datasets/ist-daten-sbb/records',
            'params': {
                'limit': '20',
                'refine_1': 'verkehrsmittel_text:"IC"',
                'refine_2': 'ankunftsverspatung:"true"',
            }
        }
    }

    if data_type not in endpoints:
        agent.send_output(
            agent_output_name='sbb_output',
            agent_result={'error': f'Invalid data_type: {data_type}. Choose from departures, cancellations, delays.'}
        )
        return

    
    endpoint_info = endpoints[data_type]
    # Transform parameter keys if needed
    params = {}
    for k, v in endpoint_info['params'].items():
        if k.startswith('refine'):
            # backend expects multiple refine parameters, not as dict keys
            if 'refine' not in params:
                params['refine'] = []
            params['refine'].append(v)
        else:
            params[k] = v
    # Expand refine list for requests
    req_params = {}
    for k, v in params.items():
        if k == 'refine' and isinstance(v, list):
            for refine_val in v:
                req_params.setdefault('refine', []).append(refine_val)
        else:
            req_params[k] = v

    # requests will flatten 'refine' if it's a list
    result = fetch_sbb_data(endpoint_info['endpoint'], req_params)

    agent.send_output(
        agent_output_name='sbb_output',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='SBBIntercityTrafficNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
