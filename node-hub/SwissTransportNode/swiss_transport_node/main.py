# Dependencies:
# pip install requests python-dotenv

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env.secret if present
load_dotenv('.env.secret')

API_BASE_URL = "http://transport.opendata.ch/v1"
DEFAULT_STATION = "Aarau"
DEFAULT_STATIONBOARD_LIMIT = 10
DEFAULT_QUERY = "Basel"
DEFAULT_ROUTE_FROM = "Lausanne"
DEFAULT_ROUTE_TO = "Genève"

@run_agent
def run(agent: MofaAgent):
    # Input contract:
    #   input_type: str, expected values: 'stationboard', 'locations', 'connections'
    #   params: dict, keys depend on input_type
    try:
        # Accept a trigger to facilitate upstream calls
        user_input = agent.receive_parameter('user_input')  # Always enable chaining
        input_type = agent.receive_parameter('input_type')  # 'stationboard', 'locations', 'connections'
        params_str = agent.receive_parameter('params')      # JSON string or dict

        import json
        try:
            params = json.loads(params_str)
        except Exception:
            params = {}

        if input_type == 'stationboard':
            # Params: station (default: Aarau), limit (int, optional)
            station = params.get('station', DEFAULT_STATION)
            try:
                limit = int(params.get('limit', DEFAULT_STATIONBOARD_LIMIT))
            except Exception:
                limit = DEFAULT_STATIONBOARD_LIMIT
            endpoint = f"{API_BASE_URL}/stationboard?station={station}&limit={limit}"
            r = requests.get(endpoint)
            r.raise_for_status()
            result = r.json()
            agent.send_output(
                agent_output_name='stationboard',
                agent_result=result
            )
        elif input_type == 'locations':
            # Params: query (default: Basel)
            query = params.get('query', DEFAULT_QUERY)
            endpoint = f"{API_BASE_URL}/locations?query={query}"
            r = requests.get(endpoint)
            r.raise_for_status()
            result = r.json()
            agent.send_output(
                agent_output_name='locations',
                agent_result=result
            )
        elif input_type == 'connections':
            # Params: from (default: Lausanne), to (default: Genève)
            route_from = params.get('from', DEFAULT_ROUTE_FROM)
            route_to = params.get('to', DEFAULT_ROUTE_TO)
            endpoint = f"{API_BASE_URL}/connections?from={route_from}&to={route_to}"
            r = requests.get(endpoint)
            r.raise_for_status()
            result = r.json()
            agent.send_output(
                agent_output_name='connections',
                agent_result=result
            )
        else:
            agent.send_output('error', {
                'error': f"Unsupported input_type: {input_type}"
            })
    except Exception as e:
        agent.send_output('error', {
            'error': str(e)
        })

def main():
    agent = MofaAgent(agent_name='SwissTransportNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
