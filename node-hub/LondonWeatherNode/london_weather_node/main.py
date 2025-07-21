from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent to fetch current weather data from wttr.in for London.
    wttr.in provides weather data via HTTP GET in JSON format.
    """
    # Facilitate dataflow compatibility (no input required, but included for consistency)
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = 'https://wttr.in/London?format=j1'
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Ensure response is JSON
        data = response.json()
        # Send the raw JSON as output; ensure serialization
        agent.send_output(
            agent_output_name='weather_json',
            agent_result=data
        )
    except Exception as e:
        # Output error in a serializable format
        agent.send_output(
            agent_output_name='weather_json',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='LondonWeatherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
