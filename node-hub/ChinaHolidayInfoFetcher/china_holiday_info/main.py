from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this agent; compatibility input (not used)
    user_input = agent.receive_parameter('user_input')
    
    # API Endpoint configuration
    API_ENDPOINT = "https://api.jiejiariapi.com/v1/holidays/2024"
    TIMEOUT = 30  # seconds
    RETRIES = 3

    response_json = None
    error_message = None

    for attempt in range(RETRIES):
        try:
            resp = requests.get(API_ENDPOINT, timeout=TIMEOUT)
            resp.raise_for_status()
            # Expect response to be serializable JSON
            response_json = resp.json()
            break  # Exit loop if successful
        except Exception as e:
            error_message = str(e)
            continue

    if response_json is not None:
        # Output data through standardized port
        agent.send_output(
            agent_output_name='china_holiday_data',
            agent_result=response_json
        )
    else:
        # Send error message if all attempts failed
        agent.send_output(
            agent_output_name='china_holiday_data',
            agent_result={"error": error_message or "Unknown error"}
        )

def main():
    agent = MofaAgent(agent_name='ChinaHolidayInfoFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
