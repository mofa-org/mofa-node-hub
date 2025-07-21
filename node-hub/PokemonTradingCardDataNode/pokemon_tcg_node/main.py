from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Required dependencies:
# - requests
# (Install via: pip install requests)

API_ENDPOINT = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
API_TIMEOUT = 30  # seconds

def fetch_card_data(params=None):
    """
    Helper function to call the Pokemon Trading Card API endpoint.
    If filtering is needed, pass query params as a dict.
    Returns the API response as a dict, or error info.
    """
    if params is None:
        params = {}
    try:
        response = requests.get(API_ENDPOINT, params=params, timeout=API_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {"error": True, "message": str(e)}

@run_agent
def run(agent: MofaAgent):
    """
    Receives optional filter parameters as a serialized string (JSON or url-encoded query string) through the 'filter_params' port.
    If absent or empty, fetches all Pokemon TCG card data.
    Outputs data through the 'card_data' port.
    """
    try:
        # Receive a string (should be a JSON or query string for filtering, or empty)
        filter_params = agent.receive_parameter('filter_params')
        # If completely empty, facilitate call by other nodes as required
        user_input = agent.receive_parameter('user_input')
        if filter_params:
            # Attempt to parse as JSON first, fallback to query string
            import json, urllib.parse
            try:
                params = json.loads(filter_params)
                if not isinstance(params, dict):
                    raise ValueError('filter_params JSON is not a dict')
            except Exception:
                # Try query string parse
                params = dict(urllib.parse.parse_qsl(filter_params))
        else:
            params = {}

        data = fetch_card_data(params)
        # Ensure serializable output
        if not isinstance(data, (dict, list)):
            data = str(data)

        agent.send_output(
            agent_output_name="card_data",
            agent_result=data
        )
    except Exception as err:
        agent.send_output(
            agent_output_name="card_data",
            agent_result={"error": True, "message": f"Agent error: {err}"}
        )

def main():
    agent = MofaAgent(agent_name='PokemonTradingCardDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
