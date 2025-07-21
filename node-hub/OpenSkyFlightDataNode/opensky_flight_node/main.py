from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import logging
from typing import Any

# Dependencies: requests
#   pip install requests

OPEN_SKY_ENDPOINTS = {
    'switzerland_airplanes': 'https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226',
    'frankfurt_arrivals': 'https://opensky-network.org/api/flights/arrival?airport=EDDF&begin=1517227200&end=1517230800',
    'all_states': 'https://opensky-network.org/api/states/all'
}

DEFAULT_TIMEOUT = 30  # seconds
ENABLE_LOGGING = True

def setup_logging():
    if ENABLE_LOGGING:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

@run_agent
def run(agent: MofaAgent):
    setup_logging()
    # Facilitate pipeline input for compatibility, even if not used
    user_input = agent.receive_parameter('user_input')
    try:
        # Receive API selection parameter
        api_choice = agent.receive_parameter('api_choice')  # one of 'switzerland_airplanes', 'frankfurt_arrivals', 'all_states'
        
        if api_choice not in OPEN_SKY_ENDPOINTS:
            result = {'error': True, 'message': f'Invalid api_choice: {api_choice}. Must be one of {list(OPEN_SKY_ENDPOINTS.keys())}.'}
            agent.send_output('flight_data', result)
            return

        endpoint = OPEN_SKY_ENDPOINTS[api_choice]
        logging.info(f"Requesting OpenSky API endpoint: {endpoint}")
        
        try:
            response = requests.get(endpoint, timeout=DEFAULT_TIMEOUT)
        except Exception as e:
            result = {'error': True, 'message': f'HTTP request failed: {str(e)}'}
            agent.send_output('flight_data', result)
            return
        
        try:
            data = response.json() if 'application/json' in response.headers.get('Content-Type', '') else response.text
        except Exception as e:
            data = response.text  # fallback to raw text
        
        if response.status_code == 200:
            processed = {'error': False, 'data': data}
        else:
            processed = {'error': True, 'status_code': response.status_code, 'data': data}
        agent.send_output(
            agent_output_name='flight_data',
            agent_result=processed
        )
    except Exception as err:
        logging.error(f"Unhandled agent error: {err}")
        result = {'error': True, 'message': f'Unhandled exception: {str(err)}'}
        agent.send_output('flight_data', result)

def main():
    agent = MofaAgent(agent_name='OpenSkyFlightDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
