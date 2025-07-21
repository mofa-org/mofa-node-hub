from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate framework input even if none required
    user_input = agent.receive_parameter('user_input')

    endpoint = "https://mcinenews.net/LAT/"
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        api_result = response.text  # API returns string content; can be JSON or HTML
    except Exception as e:
        api_result = f"ERROR: {str(e)}"

    agent.send_output(
        agent_output_name='location_api_response',
        agent_result=str(api_result)
    )

def main():
    agent = MofaAgent(agent_name='LocationCoordinateNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
