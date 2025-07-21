# Dependencies:
#   requests
# Ensure you add 'requests' to requirements.txt or your package list.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    Stateless phone number validation agent using NumLookupAPI.
    Receives 'phone_number' parameter (string).
    Outputs validation result as dictionary via 'validation_result' port.
    Handles all errors internally, returns informative error message and status in output.
    Environment: Requires NUMLOOKUP_API_KEY in .env.secret
    """
    # Input handling: receive input from calling node (required for dora-rs compliance)
    user_input = agent.receive_parameter('user_input') # Facilitate upstream call, even if unused
    try:
        phone_number = agent.receive_parameter('phone_number')
    except Exception as e:
        agent.send_output(
            agent_output_name='validation_result',
            agent_result={'success': False, 'error': f'Missing phone_number parameter: {str(e)}'}
        )
        return

    # Type check: all inputs are string, but extra care
    if not isinstance(phone_number, str) or not phone_number.strip():
        agent.send_output(
            agent_output_name='validation_result',
            agent_result={'success': False, 'error': 'Invalid phone_number input (must be non-empty string).'}
        )
        return

    # Read sensitive environment variable
    api_key = os.getenv('NUMLOOKUP_API_KEY')
    if not api_key:
        agent.send_output(
            agent_output_name='validation_result',
            agent_result={'success': False, 'error': 'API Key not provided. Please set NUMLOOKUP_API_KEY in .env.secret.'}
        )
        return

    # Use default country code 'BD', enable to override via config if necessary
    country_code = 'BD'
    base_url = 'https://api.numlookupapi.com/v1/validate/'
    url = f"{base_url}{phone_number}?apikey={api_key}&country_code={country_code}"

    try:
        response = requests.get(url, timeout=30)
    except Exception as request_exc:
        agent.send_output(
            agent_output_name='validation_result',
            agent_result={'success': False, 'error': f'HTTP connection error: {str(request_exc)}'}
        )
        return
    try:
        resp_obj = response.json()
    except Exception as json_exc:
        agent.send_output(
            agent_output_name='validation_result',
            agent_result={'success': False, 'error': f'Invalid JSON response from API: {str(json_exc)}', 'http_status_code': response.status_code}
        )
        return

    # Check API errors
    if response.status_code != 200 or resp_obj.get('error'):
        agent.send_output(
            agent_output_name='validation_result',
            agent_result={'success': False,
                         'error': resp_obj.get('msg', 'API returned an error.'),
                         'http_status_code': response.status_code,
                         'resp_obj': resp_obj}
        )
        return

    # Success case: return phone validation info (strip sensitive data if needed)
    agent.send_output(
        agent_output_name='validation_result',
        agent_result={
            'success': True,
            'result': resp_obj
        }
    )

def main():
    agent = MofaAgent(agent_name='PhoneNumberValidationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
