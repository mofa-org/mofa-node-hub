# Dependencies: requests
# If not present, install via: pip install requests
# No sensitive config; base_url/timeouts inline; logging optional.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import logging

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling (get API type and param)
        params = agent.receive_parameters(['query_type', 'value'])
        query_type = params.get('query_type', '').strip().lower()  # hex, rgb, scheme_hex, scheme_rgb
        value = params.get('value', '').strip()

        base_url = "https://www.thecolorapi.com"
        timeout = 10  # seconds
        # Optional: toggle debug logging here
        enable_logging = True
        if enable_logging:
            logging.basicConfig(level=logging.INFO)

        url = None
        if query_type == 'rgb':
            url = f"{base_url}/id?rgb={value}"
        elif query_type == 'hex':
            url = f"{base_url}/id?hex={value}"
        elif query_type == 'scheme_hex':
            # This defaults to mode=triad&count=6
            url = f"{base_url}/scheme?hex={value}&mode=triad&count=6"
        elif query_type == 'scheme_rgb':
            url = f"{base_url}/scheme?rgb={value}"
        else:
            agent.send_output('color_api_output', {'error': 'Invalid query_type. Choose rgb, hex, scheme_hex, or scheme_rgb.'})
            return

        if enable_logging:
            logging.info(f"Requesting URL: {url}")
        response = requests.get(url, timeout=timeout)

        try:
            data = response.json()
        except Exception as json_exc:
            agent.send_output('color_api_output', {'error': 'Response parsing failed', 'details': str(json_exc)})
            return

        # Handle HTTP errors
        if not response.ok or 'error' in data:
            agent.send_output('color_api_output', {'error': 'API Error', 'status_code': response.status_code, 'api_details': data})
            return

        # Pass data through (dict)
        agent.send_output(
            agent_output_name='color_api_output',
            agent_result=data
        )
    except Exception as e:
        agent.send_output('color_api_output', {'error': 'Unhandled agent error', 'details': str(e)})

def main():
    agent = MofaAgent(agent_name='ColorApiNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
