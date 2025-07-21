from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

# Dependencies: requests
# Ensure you have 'requests' in your environment for this agent.
# All input/output follows mofa/dora-rs conventions.

API_BASE_URL = "https://api.vatcomply.com"

def fetch(endpoint, params=None):
    try:
        url = f"{API_BASE_URL}{endpoint}"
        # Secure: only GET requests; no secrets exposed
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        # Ensure output is serializable
        return resp.json()
    except Exception as err:
        return {'error': str(err)}

@run_agent
def run(agent: MofaAgent):
    # For stateless API: one of the following 
    action = agent.receive_parameter('action')  # one of 'rates', 'base_rates', 'currencies', 'historical_rates', 'vat', 'geolocate'
    params = agent.receive_parameters(['base', 'date', 'vat_number'])  # All string, may be empty

    result = None

    try:
        if action == 'rates':
            # Endpoint: /rates (default rates)
            result = fetch('/rates')
        elif action == 'base_rates':
            # Endpoint: /rates?base=USD
            base = params.get('base')
            if base:
                result = fetch('/rates', {'base': base})
            else:
                result = {'error': "Missing 'base' parameter for base_rates."}
        elif action == 'currencies':
            # Endpoint: /currencies
            result = fetch('/currencies')
        elif action == 'historical_rates':
            # Endpoint: /rates?date=YYYY-MM-DD
            date = params.get('date')
            if date:
                result = fetch('/rates', {'date': date})
            else:
                result = {'error': "Missing 'date' parameter for historical_rates."}
        elif action == 'vat':
            # Endpoint: /vat?vat_number=...
            vat_number = params.get('vat_number')
            if vat_number:
                result = fetch('/vat', {'vat_number': vat_number})
            else:
                result = {'error': "Missing 'vat_number' parameter for vat validation."}
        elif action == 'geolocate':
            # Endpoint: /geolocate
            result = fetch('/geolocate')
        else:
            result = {'error': "Invalid action parameter."}
    except Exception as e:
        result = {'error': str(e)}

    # Output delivery
    agent.send_output(
        agent_output_name='vatcomply_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='VatComplyCurrencyNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
