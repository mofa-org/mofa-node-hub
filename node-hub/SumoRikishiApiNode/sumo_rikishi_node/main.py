from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# Optional: For API endpoint/config, specify defaults or read from config
def get_api_config():
    # Default values as per the given config
'try:
        endpoint = "https://www.sumo-api.com/api/rikishis" # hard-coded, or could come from os.environ if .env.secret is used
        limit = int(os.environ.get("SUMO_API_LIMIT", "100"))
        skip = int(os.environ.get("SUMO_API_SKIP", "0"))
        return endpoint, limit, skip
    except Exception:
        # On any error, fall back to reasonable defaults
        return ("https://www.sumo-api.com/api/rikishis", 100, 0)

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameters as STRINGS; convert as needed
        params = agent.receive_parameters(['limit', 'skip'])
        # Type conversion with fallback to config/defaults
        endpoint, default_limit, default_skip = get_api_config()

        limit_str = params.get('limit', str(default_limit))
        skip_str = params.get('skip', str(default_skip))
        try:
            limit = int(limit_str)
        except Exception:
            limit = default_limit
        try:
            skip = int(skip_str)
        except Exception:
            skip = default_skip

        # Safe, bounded limits per API docs
        limit = max(1, min(1000, limit))
        skip = max(0, skip)

        response = requests.get(
            endpoint,
            params={
                'limit': limit,
                'skip': skip
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()  # Should be dict/list per API
        # Ensure serializability
        agent.send_output(
            agent_output_name='rikishi_data',
            agent_result=data
        )
    except Exception as e:
        err_msg = {'error': True, 'message': str(e)}
        agent.send_output(
            agent_output_name='rikishi_data',
            agent_result=err_msg
        )

def main():
    agent = MofaAgent(agent_name='SumoRikishiApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
