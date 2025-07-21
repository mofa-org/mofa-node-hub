from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate input reception for compatibility
        user_input = agent.receive_parameter('user_input')

        # Endpoint and parameters
        url = "https://openwhyd.org/hot/electro"
        params = {"format": "json"}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Ensure output is serializable
        agent.send_output(
            agent_output_name='hot_electro_music',
            agent_result=data
        )
    except Exception as e:
        # Error containment and safe messaging
        error_msg = {"error": True, "message": str(e)}
        agent.send_output(
            agent_output_name='hot_electro_music',
            agent_result=error_msg
        )

def main():
    agent = MofaAgent(agent_name='HotElectroMusicNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
