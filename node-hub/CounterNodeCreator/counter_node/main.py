# Dependency: requests (install via pip if not present)
# dora-rs framework core agent code
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

def safe_parse_dict(param_str):
    try:
        return json.loads(param_str)
    except Exception as e:
        return None

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # for dataflow compatibility
    # Counter API endpoints
    create_url = 'https://letscountapi.com/freepublicapis/123'
    get_url = 'https://letscountapi.com/freepublicapis/123'

    # Accept 'operation' parameter: 'create' or 'get'
    params = agent.receive_parameters(['operation', 'payload'])

    result = {}
    try:
        op = params.get('operation', '').strip().lower()
        payload = params.get('payload', '')
        if op == 'create':
            # Expected JSON for payload
            data = safe_parse_dict(payload)
            if not isinstance(data, dict):
                raise ValueError('Payload is not valid JSON object.')
            response = requests.post(create_url, json=data, timeout=10)
            response.raise_for_status()
            result['status_code'] = response.status_code
            try:
                result['content'] = response.json()
            except Exception:
                result['content'] = response.text
        elif op == 'get':
            response = requests.get(get_url, timeout=10)
            response.raise_for_status()
            try:
                result['content'] = response.json()
            except Exception:
                result['content'] = response.text
            result['status_code'] = response.status_code
        else:
            result = {'error': 'Invalid operation. Use "create" or "get".'}
    except Exception as e:
        result = {'error': str(e)}

    agent.send_output(
        agent_output_name='counter_api_result',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='CounterNodeCreator')
    run(agent=agent)

if __name__ == '__main__':
    main()
