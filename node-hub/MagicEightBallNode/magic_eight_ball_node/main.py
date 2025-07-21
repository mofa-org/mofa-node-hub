from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Add this to facilitate calls from other nodes even though the API needs no true input
    user_input = agent.receive_parameter('user_input')

    api_url = "https://m8b.gamerselimiko.workers.dev"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The API typically returns JSON
        api_result = response.json()
        # Ensure serialization
        if not isinstance(api_result, (dict, list, str)):
            api_result = str(api_result)
        agent.send_output(
            agent_output_name='magic_eight_ball_response',
            agent_result=api_result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='magic_eight_ball_response',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='MagicEightBallNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
