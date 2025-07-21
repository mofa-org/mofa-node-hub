from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes to call this agent, even though no input required:
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = "https://radio-basilisk.api.radiosphere.io/channels/87d0aaab-1db2-453b-af40-63bdde8cd1d1/track-history"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # try to return JSON if possible, fallback to string
        try:
            data = response.json()
        except Exception:
            data = response.text
        agent.send_output(
            agent_output_name='track_history',
            agent_result=data
        )
    except Exception as e:
        # Compose error message for output
        err = {'error': True, 'msg': str(e)}
        agent.send_output(
            agent_output_name='track_history',
            agent_result=err
        )

def main():
    agent = MofaAgent(agent_name='RadioBasiliskTrackHistoryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies
# - requests
# Ensure 'requests' is available, add to requirements.txt if packaging.
