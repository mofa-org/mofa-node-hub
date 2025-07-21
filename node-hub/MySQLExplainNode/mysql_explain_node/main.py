from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    MySQLExplainNode: Provides two main endpoints via mysqlexplain.com API -
    1. oEmbed: GET request to retrieve iframe embed code for an EXPLAIN plan.
    2. explains: POST request to submit a MySQL EXPLAIN for analysis.

    Input Ports:
        action:   str ('oembed' or 'submit_explain')
        # oembed requires:
            url: str (url to the EXPLAIN plan)
            showFullscreenButton: str ('true'/'false'), optional (default: 'true')
        # submit_explain requires:
            query: str (MySQL query), optional (default 'SELECT 1')
            version: str, optional
            bindings: json str, optional (default: [])
            explain_json: json str, optional (default: {})
            explain_tree: json str, optional (default: {})
    Output Ports:
        result: dict or str (API response)
    """
    try:
        # Facilitate dataflow even if no input is required
        user_input = agent.receive_parameter('user_input')
        params = agent.receive_parameters(['action','url','showFullscreenButton','query','version','bindings','explain_json','explain_tree'])
        action = params.get('action', '').strip().lower()
        
        if action == 'oembed':
            url = params.get('url', '')
            show_fullscreen = params.get('showFullscreenButton', 'true')
            endpoint = 'https://api.mysqlexplain.com/v2/oembed.json'
            query_params = {
                'url': url,
                'showFullscreenButton': show_fullscreen
            }
            response = requests.get(endpoint, params=query_params, timeout=15)
            response.raise_for_status()
            result = response.json()
            agent.send_output('result', result)
        elif action == 'submit_explain':
            endpoint = 'https://api.mysqlexplain.com/v2/explains'
            query = params.get('query', 'SELECT 1')
            version = params.get('version', '')

            # Convert JSON string fields to objects
            def safe_json_loads(val, default):
                if not val:
                    return default
                try:
                    return json.loads(val)
                except Exception:
                    return default

            bindings = safe_json_loads(params.get('bindings'), [])
            explain_json = safe_json_loads(params.get('explain_json'), {})
            explain_tree = safe_json_loads(params.get('explain_tree'), {})
            post_body = {
                'query': query,
                'version': version,
                'bindings': bindings,
                'explain_json': explain_json,
                'explain_tree': explain_tree
            }
            # Remove empty fields to avoid overwriting server defaults
            post_body = {k: v for k, v in post_body.items() if v not in ['', [], {}]}

            response = requests.post(endpoint, json=post_body, timeout=20)
            response.raise_for_status()
            result = response.json()
            agent.send_output('result', result)
        else:
            agent.send_output('result', {'error': 'Invalid action specified. Use "oembed" or "submit_explain".'})
    except Exception as e:
        agent.send_output('result', {'error': str(e)})

def main():
    agent = MofaAgent(agent_name='MySQLExplainNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
