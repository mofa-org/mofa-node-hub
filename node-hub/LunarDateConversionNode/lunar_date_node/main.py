from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive 'date' parameter as required by API (expected format: YYYY-MM-DD)
        date_str = agent.receive_parameter('date')
        if not date_str:
            # If no date provided, inform downstream nodes; API requires a date
            agent.send_output(
                agent_output_name='lunar_date_response',
                agent_result={
                    'error': 'Missing required parameter: date (format YYYY-MM-DD)'
                }
            )
            return
        # Prepare API request
        endpoint = 'https://data.weather.gov.hk/weatherAPI/opendata/lunardate.php'
        params = {'date': date_str}
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()  # Should already be serializable
        except Exception as api_err:
            agent.send_output(
                agent_output_name='lunar_date_response',
                agent_result={
                    'error': f'API request failed: {str(api_err)}'
                }
            )
            return
        # Output the API result
        agent.send_output(
            agent_output_name='lunar_date_response',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='lunar_date_response',
            agent_result={'error': f'Internal error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='LunarDateConversionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
#
# Ensure the requests package is available in your environment.
#
# Input ports:
#   date: string, required, format YYYY-MM-DD
# Output ports:
#   lunar_date_response: dict (API response or error message)
