from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    GuildWarsBuildNode Agent:
    Fetches the current build information from the Guild Wars 2 API endpoint.
    No input is required for this node, but for compatibility, we include user_input reception.
    Output:
        Sends API response (as dict) to 'build_info' dataflow port.
    Dependencies:
        - requests
    """
    try:
        # Compatibility input (needed for chaining):
        user_input = agent.receive_parameter('user_input')  # Node does not use it, included for dataflow compatibility

        endpoint = "https://api.guildwars2.com/v2/build"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Expecting a small dict or string from this endpoint
        data = response.json()

        agent.send_output(
            agent_output_name='build_info',
            agent_result=data  # dict is serializable
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='build_info',
            agent_result={'error': f'Failed to fetch build data: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='GuildWarsBuildNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
