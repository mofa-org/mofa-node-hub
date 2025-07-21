from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Get uid parameter from input (as string), or use default if not provided
        uid = agent.receive_parameter('uid')
        if not uid or uid.strip() == '':
            # fallback to hardcoded default UID
            uid = 'SAMA0000001633'
        endpoint = 'https://stapi.co/api/v1/rest/season'
        params = {'uid': uid}

        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception:
            data = response.text

        # Output node: data must be serializable
        agent.send_output(
            agent_output_name='season_info',
            agent_result=data
        )
    except Exception as e:
        # Error handling: send error info out
        agent.send_output(
            agent_output_name='season_info',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='StarTrekSeasonNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
