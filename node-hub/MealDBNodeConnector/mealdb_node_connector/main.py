# Dependencies:
#   - requests
#   - python-dotenv (if you want to support .env.secret for future extensibility)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

API_BASE_URL = "https://www.themealdb.com/api/json/v1/1/"
DEFAULT_TIMEOUT = 15
RETRY_COUNT = 2

def build_url(endpoint_path: str, params: dict = None) -> str:
    url = API_BASE_URL + endpoint_path
    if params:
        param_str = '&'.join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{param_str}"
    return url

def perform_get_request(url: str, timeout: int = DEFAULT_TIMEOUT, retries: int = RETRY_COUNT):
    last_exc = None
    for _ in range(retries):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            last_exc = exc
    raise last_exc

@run_agent
def run(agent: MofaAgent):
    # User input expected: 'action' (str: 'random_meal', 'search_by_name', 'list_by_first_letter', 'filter_by_ingredient')
    # Depending on action, expects another parameter. All parameters must be string type.
    try:
        params = agent.receive_parameters(['action', 'value'])  # 'value' can be name, letter, or ingredient
        action = params.get('action', '').strip().lower()
        value = params.get('value', '').strip()
        result = None

        if action == 'random_meal':
            url = API_BASE_URL + 'random.php'
            result = perform_get_request(url)
        elif action == 'search_by_name':
            url = build_url('search.php', {'s': value})
            result = perform_get_request(url)
        elif action == 'list_by_first_letter':
            if not value or len(value) != 1 or not value.isalpha():
                raise ValueError("'value' must be a single letter for 'list_by_first_letter' action.")
            url = build_url('search.php', {'f': value})
            result = perform_get_request(url)
        elif action == 'filter_by_ingredient':
            if not value:
                raise ValueError("'value' must be a non-empty ingredient name for 'filter_by_ingredient' action.")
            url = build_url('filter.php', {'i': value})
            result = perform_get_request(url)
        else:
            raise ValueError(f"Unknown action: {action}")

        # Ensure serializable output
        agent.send_output(
            agent_output_name='mealdb_result',
            agent_result=result
        )
    except Exception as exc:
        # Error output for debugging
        agent.send_output(
            agent_output_name='mealdb_result',
            agent_result={
                'error': True,
                'error_message': str(exc)
            }
        )

def main():
    agent = MofaAgent(agent_name='MealDBNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
