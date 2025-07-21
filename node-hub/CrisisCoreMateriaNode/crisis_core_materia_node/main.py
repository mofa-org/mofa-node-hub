# Dependencies: requests
# Place 'requests' in requirements.txt or the agent dependency section.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

API_BASE = "https://crisis-core-materia-fusion-api-546461677134.us-central1.run.app"

@run_agent
def run(agent: MofaAgent):
    """
    DORA-RS compliant agent for Crisis Core Materia API.
    Supported actions:
    - get_materia_list: List all materia
    - health_check: Check API health
    - fuse_materia: Fuse two materia (requires input params)
    """
    try:
        params = agent.receive_parameters(['action', 'materia1', 'materia2'])
        action = params.get('action', '').strip().lower()
    except Exception as e:
        agent.send_output('error', {'error': f'Parameter reception failed: {str(e)}'})
        return

    # Stateless branching by action
    try:
        if action == 'get_materia_list':
            resp = requests.get(f"{API_BASE}/materia", timeout=30)
            resp.raise_for_status()
            result = resp.json()
            agent.send_output('materia_list', result)
            return
        elif action == 'health_check':
            resp = requests.get(f"{API_BASE}/status", timeout=10)
            resp.raise_for_status()
            result = resp.json()
            agent.send_output('health_status', result)
            return
        elif action == 'fuse_materia':
            # Both materia1 and materia2 are required
            materia1 = params.get('materia1', '').strip()
            materia2 = params.get('materia2', '').strip()
            if not materia1 or not materia2:
                agent.send_output(
                    'fusion_result',
                    {'error': 'Missing required parameters: materia1 and materia2 must be non-empty strings.'}
                )
                return
            payload = {
                "materia1": materia1,
                "materia2": materia2
            }
            headers = {'Content-Type': 'application/json'}
            resp = requests.post(f"{API_BASE}/fusion", data=json.dumps(payload), headers=headers, timeout=30)
            resp.raise_for_status()
            fusion_result = resp.json()
            agent.send_output('fusion_result', fusion_result)
            return
        else:
            agent.send_output('error', {'error': f"Unknown action: {action}"})
            return
    except requests.exceptions.Timeout:
        agent.send_output('error', {'error': 'API request timed out.'})
        return
    except requests.exceptions.HTTPError as e:
        agent.send_output('error', {'error': f'HTTP error: {str(e)}', 'details': getattr(e.response, 'text', None)})
        return
    except Exception as e:
        agent.send_output('error', {'error': f'Unexpected error: {str(e)}'})
        return

def main():
    agent = MofaAgent(agent_name='CrisisCoreMateriaNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
