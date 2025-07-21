from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameters as strings
        params = agent.receive_parameters(['year', 'country'])
        year_str = params.get('year')
        country = params.get('country')

        # Fallback/defaults if not provided
        if not year_str:
            year_str = '2024'
        if not country:
            country = 'CH'

        # Type conversion: ensure year is an integer
        try:
            year = int(year_str)
        except (ValueError, TypeError):
            agent.send_output(
                agent_output_name='error',
                agent_result=f"Invalid year format: {year_str}"
            )
            return

        api_url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country}"
        try:
            resp = requests.get(api_url, timeout=10)
            resp.raise_for_status()
            holidays = resp.json()  # Should be serializable (list/dict)
        except requests.RequestException as req_err:
            agent.send_output(
                agent_output_name='error',
                agent_result=f"API request error: {str(req_err)}"
            )
            return
        except json.JSONDecodeError as jde:
            agent.send_output(
                agent_output_name='error',
                agent_result=f"Response decoding error: {str(jde)}"
            )
            return

        # Success: Send holiday list (serializable)
        agent.send_output(
            agent_output_name='holidays',
            agent_result=holidays
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result=f"Unexpected error: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='PublicHolidayAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   - requests
