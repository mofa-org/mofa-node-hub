# Dependencies: requests
# Ensure 'requests' is included in requirements. No extra files are required.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

MATERIA_LIST_URL = "https://crisis-core-materia-fusion-api-546461677134.us-central1.run.app/materia"
HEALTH_CHECK_URL = "https://crisis-core-materia-fusion-api-546461677134.us-central1.run.app/status"
FUSION_URL = "https://crisis-core-materia-fusion-api-546461677134.us-central1.run.app/fusion"
REQUEST_TIMEOUT = 30

@run_agent
def run(agent: MofaAgent):
    """
    This agent supports three operations:
    1. List all materia (action = 'list')
    2. Health check (action = 'health')
    3. Fuse two materia (action = 'fuse', expects payload as JSON string: '{"materia_a":..., "materia_b":...}')
    Input: receive_parameters(['action', 'payload'])
    Output: via port matching output_type (see code below)
    """
    try:
        params = agent.receive_parameters(['action', 'payload'])
        action = params.get('action', '').strip().lower()
        payload_str = params.get('payload', None)

        if action == 'list':
            response = requests.get(MATERIA_LIST_URL, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            try:
                output = response.json()
            except Exception:
                output = response.text
            agent.send_output('materia_list', output)

        elif action == 'health':
            response = requests.get(HEALTH_CHECK_URL, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            try:
                output = response.json()
            except Exception:
                output = response.text
            agent.send_output('health_status', output)

        elif action == 'fuse':
            if not payload_str:
                agent.send_output('fusion_result', {'error':'Missing payload for fusion.'})
                return
            try:
                # User must send JSON string: '{"materia_a":..., "materia_b":...}'
                data = json.loads(payload_str)
            except Exception as e:
                agent.send_output('fusion_result', {'error': f'Invalid JSON payload: {e}'})
                return
            response = requests.post(FUSION_URL, json=data, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            try:
                output = response.json()
            except Exception:
                output = response.text
            agent.send_output('fusion_result', output)
        else:
            agent.send_output('invalid_action', {'error': 'Invalid action specified.'})
    except Exception as e:
        agent.send_output('error', {'error': str(e)})

def main():
    agent = MofaAgent(agent_name='MateriaFusionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
