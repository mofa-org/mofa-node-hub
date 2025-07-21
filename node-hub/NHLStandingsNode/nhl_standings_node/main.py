# Dependencies: requests (install via `pip install requests`)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitator input (no actual input, ensures dataflow compatibility)
    user_input = agent.receive_parameter('user_input')
    
    # NHL standings endpoint
    endpoint = "https://api-web.nhle.com/v1/standings-season"
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Try to get JSON output; fallback to string if not serializable
        try:
            standings_data = response.json()
        except Exception:
            standings_data = response.text
        # Output as dict or string, must be serializable
        agent.send_output(
            agent_output_name='nhl_standings',
            agent_result=standings_data
        )
    except Exception as err:
        # Graceful error reporting
        agent.send_output(
            agent_output_name='nhl_standings',
            agent_result={
                'error': True,
                'message': f'Failed to retrieve NHL standings: {str(err)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='NHLStandingsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
