from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os
import json

# --- Dependency: requests ---
# Install: pip install requests

OEC_API_BASE_URL = "https://oec.world/api/olap-proxy/data.jsonrecords"
DEFAULT_LOCALE = "en"

@run_agent
def run(agent: MofaAgent):
    """
    Fetch trade data from OEC API given user parameters.

    Input Parameters via receive_parameters():
      - year (str): Data year (e.g. '2012', '2015', '2022')
      - exporter_country (str, optional): Exporter Country code (e.g. 'eufra', 'sabra')
      - drilldowns (str, optional): Comma-separated drilldowns
      - cube (str, optional): Cube specifier (default 'trade_i_baci_a_92')
      - measures (str, optional): Measures to request (default 'Trade Value,Quantity')
      - sort (str, optional): Sort string (e.g., 'Trade Value.desc')
      - properties (str, optional): Extra property string (optional, may be blank)
      - locale (str, optional): API language (default 'en')
    Output via send_output():
      - agent_output_name: 'trade_data' with dict (JSON deserialized data) or error string
    """
    try:
        # Collect parameters
        params = agent.receive_parameters([
            'year',
            'exporter_country',
            'drilldowns',
            'cube',
            'measures',
            'sort',
            'properties',
            'locale'
        ])

        # Build query params dictionary with defaults
        query = {
            'Year': params.get('year', '2022'),
            'cube': params.get('cube', 'trade_i_baci_a_92'),
            'locale': params.get('locale', DEFAULT_LOCALE),
        }
        if params.get('exporter_country'):
            query['Exporter Country'] = params['exporter_country']
        if params.get('drilldowns'):
            query['drilldowns'] = params['drilldowns']
        if params.get('measures'):
            query['measures'] = params['measures']
        else:
            query['measures'] = 'Trade Value,Quantity'
        if params.get('sort'):
            query['sort'] = params['sort']
        if params.get('properties'):
            query['properties'] = params['properties']

        # API expects drilldowns/measures as comma-separated
        # Assemble query string
        response = requests.get(OEC_API_BASE_URL, params=query, timeout=30)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as je:
            return agent.send_output(
                agent_output_name='trade_data',
                agent_result={
                    "error": "Failed to parse API response as JSON.",
                    "details": str(je)
                }
            )
        agent.send_output(
            agent_output_name='trade_data',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='trade_data',
            agent_result={
                "error": "Failed to fetch trade data from OEC API.",
                "details": str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='TradeOECDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
