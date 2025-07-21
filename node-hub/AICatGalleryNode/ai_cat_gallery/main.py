# Dependencies: requests (install via `pip install requests`)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
import json

def get_env(key, default=None):
    # Utility function for retrieving environment variable
    return os.getenv(key, default)

class AICatGalleryNodeConfig:
    BASE_URL = "https://api.ai-cats.net/v1/cat"
    TIMEOUT = 10
    DEFAULT_LIMIT = 5
    DEFAULT_SIZE = 1024
    DEFAULT_THEME = "All"
    DEFAULT_DESCENDING = False

@run_agent
def run(agent: MofaAgent):
    """
    This agent routes user requests to the ai-cats.net API for various image and info queries.
    Input ports:
        action: str      # One of ['random', 'search', 'count', 'by_id', 'similar', 'themes', 'info', 'search_completion']
        user_input: str  # See below for required value for each action
    Output ports are named for each action result.
    """
    try:
        params = agent.receive_parameters(['action', 'user_input'])  # All user_input is string (can be JSON for search)
        action = params.get('action', '').strip().lower()
        user_input = params.get('user_input', '').strip()
        cfg = AICatGalleryNodeConfig()
        output = None
        output_port = None
        headers = {'Accept': 'application/json'}

        if action == 'random':
            resp = requests.get(cfg.BASE_URL, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'random_cat'
            resp.raise_for_status()
            output = resp.json()
        elif action == 'search':
            # user_input should be a JSON string with possible keys: query, limit, size, theme, descending
            try:
                search_args = json.loads(user_input) if user_input else {}
            except Exception:
                search_args = {}
            query = search_args.get('query', '')
            limit = int(search_args.get('limit', cfg.DEFAULT_LIMIT))
            size = int(search_args.get('size', cfg.DEFAULT_SIZE))
            theme = search_args.get('theme', cfg.DEFAULT_THEME)
            descending = str(search_args.get('descending', cfg.DEFAULT_DESCENDING)).lower()
            url = f"{cfg.BASE_URL}/search"
            paramsq = {
                'query': query,
                'limit': limit,
                'size': size,
                'theme': theme,
                'descending': descending
            }
            resp = requests.get(url, params=paramsq, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'search_results'
            resp.raise_for_status()
            output = resp.json()
        elif action == 'count':
            # user_input: theme (or empty for all)
            theme = user_input or cfg.DEFAULT_THEME
            url = f"{cfg.BASE_URL}/count"
            paramsq = {'theme': theme}
            resp = requests.get(url, params=paramsq, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'cat_count'
            resp.raise_for_status()
            output = resp.json()
        elif action == 'by_id':
            # user_input: cat image's ID
            cat_id = user_input
            url = f"{cfg.BASE_URL}/{cat_id}"
            resp = requests.get(url, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'cat_by_id'
            resp.raise_for_status()
            output = resp.json()
        elif action == 'similar':
            # user_input: cat image's ID
            cat_id = user_input
            url = f"{cfg.BASE_URL}/similar/{cat_id}"
            resp = requests.get(url, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'similar_cats'
            resp.raise_for_status()
            output = resp.json()
        elif action == 'themes':
            url = f"{cfg.BASE_URL}/theme-list"
            resp = requests.get(url, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'theme_list'
            resp.raise_for_status()
            output = resp.json()
        elif action == 'info':
            # user_input: cat image's ID
            cat_id = user_input
            url = f"{cfg.BASE_URL}/info/{cat_id}"
            resp = requests.get(url, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'cat_info'
            resp.raise_for_status()
            output = resp.json()
        elif action == 'search_completion':
            # user_input should be a JSON string with possible keys: query, theme
            try:
                search_args = json.loads(user_input) if user_input else {}
            except Exception:
                search_args = {}
            query = search_args.get('query', '')
            theme = search_args.get('theme', cfg.DEFAULT_THEME)
            url = f"{cfg.BASE_URL}/search-completion"
            paramsq = {'query': query, 'theme': theme}
            resp = requests.get(url, params=paramsq, timeout=cfg.TIMEOUT, headers=headers)
            output_port = 'search_completion_suggestions'
            resp.raise_for_status()
            output = resp.json()
        else:
            output_port = 'error'
            output = {'error': 'Invalid action'}
        # All outputs must be serializable (dict/list/str)
        agent.send_output(
            agent_output_name=output_port,
            agent_result=output # Should already be serializable
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='AICatGalleryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
