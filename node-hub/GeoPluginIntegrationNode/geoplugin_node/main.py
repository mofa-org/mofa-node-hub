from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    GeoPluginIntegrationNode: Integrates with geoplugin.net public APIs for currency conversion and IP geolocation.
    Operations:
      - "mode": Either 'currency_converter' or 'ip_geolocation'
      - "base_currency": Optional parameter for currency_converter mode (default 'EUR')
    Outputs:
      - 'result': dict with deserialized JSON response from the API
    """
    try:
        params = agent.receive_parameters(['mode', 'base_currency'])
        mode = params.get('mode', '').strip().lower()
        base_currency = params.get('base_currency', 'EUR').strip().upper()
        
        if mode not in ['currency_converter', 'ip_geolocation']:
            raise ValueError("Invalid mode. Use 'currency_converter' or 'ip_geolocation'.")

        if mode == 'currency_converter':
            url = "http://www.geoplugin.net/json.gp"
            query_params = {'base_currency': base_currency}
        else:  # 'ip_geolocation'
            url = "http://www.geoplugin.net/json.gp"
            query_params = None

        try:
            response = requests.get(url, params=query_params, timeout=10)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            data = {'error': True, 'message': f'Request failed: {str(e)}'}
        
        # Validate serialization
        if not isinstance(data, (dict, list, str)):
            data = {'error': True, 'message': 'API response not serializable'}

        agent.send_output(
            agent_output_name='result',
            agent_result=data
        )

    except Exception as ex:
        agent.send_output(
            agent_output_name='result',
            agent_result={'error': True, 'message': str(ex)}
        )

def main():
    agent = MofaAgent(agent_name='GeoPluginIntegrationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests (install via pip if not available)

Usage:
- Inputs via dataflow ports: 'mode' (str: 'currency_converter' or 'ip_geolocation'), 'base_currency' (str, optional, default 'EUR')
- Output port: 'result' (JSON/dict)
"""