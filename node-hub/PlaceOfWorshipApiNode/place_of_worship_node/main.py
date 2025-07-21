from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

def get_env(key: str, default=None):
    # Utility for reading environment variables safely
    return os.getenv(key, default)

@run_agent
def run(agent: MofaAgent):
    # Input handling: requires two ports for flexible API
    try:
        query_type = agent.receive_parameter('query_type')  # 'church' or 'religion'
        entity_id = agent.receive_parameter('entity_id')    # id as string (should be integer)
    except Exception as input_exc:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': 'Input reception failed',
                'detail': str(input_exc)
            }
        )
        return
    # Type conversion
    try:
        entity_id_int = int(entity_id)
    except Exception:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': 'id must be an integer',
                'received': entity_id
            }
        )
        return

    # Load config (non-secret)
    base_url = "https://www.opensanctum.com/v1"
    timeout = 30
    max_retries = 3

    # Compose URL
    if query_type == 'church':
        endpoint = f"{base_url}/churches/id/{entity_id_int}"
    elif query_type == 'religion':
        endpoint = f"{base_url}/religion/id/{entity_id_int}"
    else:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': "Unsupported query_type provided.",
                'supported_types': ['church', 'religion']
            }
        )
        return

    session = requests.Session()
    retries = 0
    while retries < max_retries:
        try:
            resp = session.get(endpoint, timeout=timeout)
            if resp.status_code == 200:
                # Return JSON data as dict
                agent.send_output(
                    agent_output_name='api_response',
                    agent_result=resp.json()  # Already JSON serializable
                )
                return
            else:
                agent.send_output(
                    agent_output_name='api_response',
                    agent_result={
                        'error': f'API HTTP Error: {resp.status_code}',
                        'details': resp.text
                    }
                )
                return
        except Exception as exc:
            retries += 1
            if retries >= max_retries:
                agent.send_output(
                    agent_output_name='api_response',
                    agent_result={
                        'error': 'API request failed after retries',
                        'detail': str(exc)
                    }
                )
                return

def main():
    agent = MofaAgent(agent_name='PlaceOfWorshipApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
