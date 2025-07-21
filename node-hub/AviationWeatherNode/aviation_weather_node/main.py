from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Required for downstream node invocation consistency
    user_input = agent.receive_parameter('user_input')  # Not used, placeholder for interface compliance
    api_url = 'https://aviationweather.gov/api/data/airport?ids=ZRH&format=json'
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        # Return error information as a serializable string
        agent.send_output(
            agent_output_name='aviation_weather_result',
            agent_result={'error': True, 'message': str(e)}
        )
        return
    # Ensure serialization (dict)
    agent.send_output(
        agent_output_name='aviation_weather_result',
        agent_result=data
    )

def main():
    agent = MofaAgent(agent_name='AviationWeatherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
