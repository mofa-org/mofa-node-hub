from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Add dummy receive_parameter for dataflow consistency
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = "https://energy.ch/api/channels/bern/playouts"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Try parsing as JSON, else fallback to text
        try:
            data = response.json()
        except Exception:
            data = response.text
        agent.send_output(
            agent_output_name='radio_playlist_response',
            agent_result=data # should be serializable (dict or string)
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='radio_playlist_response',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='EnergyBernRadioNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
