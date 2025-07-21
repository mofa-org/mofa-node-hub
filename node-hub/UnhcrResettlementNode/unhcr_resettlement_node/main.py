"""
Agent Name: UnhcrResettlementNode
Description: Provides access to UNHCR API endpoints for regions, categories, and paginated resettlement departures data. All API requests are performed via GET. Node exposes three dataflow output ports: 'regions', 'categories', and 'departures'.

Dependencies:
- requests
- python-dotenv (if .env.secret used; not required for public endpoints)
"""
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

REGIONS_ENDPOINT = "http://api.unhcr.org/rsq/v1/regions"
CATEGORIES_ENDPOINT = "http://api.unhcr.org/rsq/v1/categories"
DEPARTURES_ENDPOINT = "http://api.unhcr.org/rsq/v1/departures"


def get_regions():
    try:
        resp = requests.get(REGIONS_ENDPOINT, timeout=20)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": f"Failed to fetch regions: {str(e)}"}


def get_categories():
    try:
        resp = requests.get(CATEGORIES_ENDPOINT, timeout=20)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": f"Failed to fetch categories: {str(e)}"}


def get_departures(params: dict):
    try:
        resp = requests.get(DEPARTURES_ENDPOINT, params=params, timeout=20)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": f"Failed to fetch departures: {str(e)}"}


@run_agent
def run(agent: MofaAgent):
    # To facilitate graph invocation, always try to receive a 'user_input' param
    user_input = agent.receive_parameter('user_input')  # Can be ignored if not needed
    # Determine which UNHCR API endpoint to call, expects parameter 'api_action' (regions/categories/departures)
    api_action = agent.receive_parameter('api_action')

    if api_action == 'regions':
        data = get_regions()
        agent.send_output('regions', data)
    elif api_action == 'categories':
        data = get_categories()
        agent.send_output('categories', data)
    elif api_action == 'departures':
        # For departures, expect additional parameters; parse and convert
        default_params = {
            "page": "1",
            "year": "2016,2017",
            "origin": "MMR,SYR",
            "asylum": "JOR,LBN",
            "resettlement": "NOR,USA"
        }
        # Allow incoming params to override defaults
        try:
            departures_params = agent.receive_parameters(["page", "year", "origin", "asylum", "resettlement"])
        except Exception:
            departures_params = {}
        for k, v in default_params.items():
            if not departures_params.get(k):
                departures_params[k] = v
        # All values must be strings
        for k in departures_params:
            departures_params[k] = str(departures_params[k])
        data = get_departures(departures_params)
        agent.send_output('departures', data)
    else:
        agent.send_output('error', {'error': 'Unknown api_action. Please specify one of: regions, categories, departures.'})

def main():
    agent = MofaAgent(agent_name='UnhcrResettlementNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
