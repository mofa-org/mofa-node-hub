# Agent: CurrencyExchangeChartNode (module: currency_exchange_chart)
# Dependencies: requests (install via pip if needed)
# Documentation: https://kekkai-docs.redume.su

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json
from datetime import datetime, timedelta

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameters required for all supported operations. Accept as dict, allow missing keys.
        params = agent.receive_parameters([
            'operation',            # 'chart_week', 'chart_period', 'rate_day', 'rate_period'
            'from_currency',        # e.g. 'RUB'
            'conv_currency',        # e.g. 'USD'
            'date',                # For single-day rate queries (YYYY-MM-DD)
            'start_date',           # Start of period (YYYY-MM-DD)
            'end_date'              # End of period (YYYY-MM-DD)
        ])
        # Type assertion/cleanup
        operation = params.get('operation', '').strip()
        from_currency = params.get('from_currency') or 'RUB'
        conv_currency = params.get('conv_currency') or 'USD'
        date = params.get('date')
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        base_url = 'https://kekkai-api.redume.su/api'
        timeout = 10 # seconds
        result = None
        url = None

        # Routing and construction
        if operation == 'chart_week':
            url = f"{base_url}/getChart/week?from_currency={from_currency}&conv_currency={conv_currency}"
            description = 'Creating a graph for the last week'
        elif operation == 'chart_period':
            if not (start_date and end_date):
                raise ValueError('Missing start_date or end_date for chart_period')
            url = f"{base_url}/getChart/?from_currency={from_currency}&conv_currency={conv_currency}&start_date={start_date}&end_date={end_date}"
            description = 'Creating a graph for a certain period'
        elif operation == 'rate_day':
            if not date:
                raise ValueError('Missing date for rate_day')
            url = f"{base_url}/getRate/?from_currency={from_currency}&conv_currency={conv_currency}&date={date}"
            description = 'Getting the currency rate for a certain day.'
        elif operation == 'rate_period':
            if not (start_date and end_date):
                raise ValueError('Missing start_date or end_date for rate_period')
            url = f"{base_url}/getRate/?from_currency={from_currency}&conv_currency={conv_currency}&start_date={start_date}&end_date={end_date}"
            description = 'Get currency exchange rate for a certain period'
        else:
            raise ValueError('Invalid operation. Supported: chart_week, chart_period, rate_day, rate_period')

        # Make the GET request
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status() # HTTP error code exception
        try:
            result = resp.json()
        except Exception as e:
            # Fallback to text if not JSON
            result = {'raw': resp.text, 'error': f'Non-JSON response: {str(e)}'}

        agent.send_output(
            agent_output_name='api_response',
            agent_result=result if isinstance(result, (dict, list)) else str(result)
        )
    except Exception as err:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': str(err),
                'inputs': params if 'params' in locals() else None
            }
        )

def main():
    agent = MofaAgent(agent_name='CurrencyExchangeChartNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
