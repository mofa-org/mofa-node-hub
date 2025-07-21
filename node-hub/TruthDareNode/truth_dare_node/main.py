from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# No input required, but facilitating connection:
def noop_user_input(agent):
    user_input = agent.receive_parameter('user_input')  # To facilitate external calls
    return user_input

@run_agent
def run(agent: MofaAgent):
    try:
        user_input = agent.receive_parameter('user_input')  # Not used, just for interface compliance
        # Get a random truth
        try:
            truth_response = requests.get('https://abhi-api.vercel.app/api/game/truth', timeout=10)
            truth_response.raise_for_status()
            truth_data = truth_response.json().get('truth', '')
        except Exception as e:
            truth_data = f"Error fetching truth: {str(e)}"
        # Get a random dare
        try:
            dare_response = requests.get('https://abhi-api.vercel.app/api/game/dare', timeout=10)
            dare_response.raise_for_status()
            dare_data = dare_response.json().get('dare', '')
        except Exception as e:
            dare_data = f"Error fetching dare: {str(e)}"
        # Results as a dict for serialization
        agent_result = {
            'truth': truth_data,
            'dare': dare_data
        }
    except Exception as err:
        agent_result = {
            'error': str(err)
        }
    agent.send_output(
        agent_output_name='truth_dare_result',
        agent_result=agent_result
    )

def main():
    agent = MofaAgent(agent_name='TruthDareNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Requirements:
# requests
