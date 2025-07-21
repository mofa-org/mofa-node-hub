from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it, even if not required here
    user_input = agent.receive_parameter('user_input')
    api_url = 'https://api.data.gov.sg/v1/environment/air-temperature'
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure output serialization
        agent.send_output(
            agent_output_name='weather_data',
            agent_result=data
        )
    except Exception as e:
        # Error containment and serializable error report
        agent.send_output(
            agent_output_name='weather_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='SingaporeWeatherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
