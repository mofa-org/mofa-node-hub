# Required dependencies:
#   requests
#   (Framework dependencies: mofa.agent_build)
# Install via:
#   pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # This node does not need explicit input, but to maintain compatibility:
    user_input = agent.receive_parameter('user_input')  # For call chain completeness, not used

    # Prepare endpoints and corresponding output port names
    endpoints = {
        'top_manga': 'https://api.jikan.moe/v4/top/manga',
        'top_anime': 'https://api.jikan.moe/v4/top/anime',
        'anime_recommendations': 'https://api.jikan.moe/v4/recommendations/anime',
        'top_people': 'https://api.jikan.moe/v4/top/people',
    }
    results = {}
    for port, url in endpoints.items():
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                # Ensure output is serializable
                agent.send_output(
                    agent_output_name=port,
                    agent_result=data
                )
                results[port] = 'OK'
            else:
                msg = f"Failed to fetch {port}: status {resp.status_code}."
                agent.send_output(
                    agent_output_name=port,
                    agent_result={'error': msg}
                )
                results[port] = 'ERROR'
        except Exception as e:
            agent.send_output(
                agent_output_name=port,
                agent_result={'error': str(e)}
            )
            results[port] = 'EXCEPTION'
    # Optionally, send overall status
    agent.send_output(
        agent_output_name='status',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='JikanTopContentNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
