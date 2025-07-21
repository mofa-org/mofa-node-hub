from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    '''
    Two main capabilities:
    1. List all obsolete cards and their functional reprints (no input required)
    2. List superior/inferior versions for a specific card name ("card_name" input required)
    '''
    user_input = agent.receive_parameter('user_input')  # For stateless chaining, always accept this as a convention
    card_name = agent.receive_parameter('card_name')
    try:
        if card_name:
            # Feature 2: Fetch obsoletes for given card
            obsoletes_url = f"https://www.strictlybetter.eu/api/obsoletes/{card_name}"
            response = requests.get(obsoletes_url, timeout=6)
            response.raise_for_status()
            output_data = response.json()
            agent.send_output(
                agent_output_name='obsoletes_result',
                agent_result=output_data
            )
        else:
            # Feature 1: List all obsolete cards and their reprints
            functional_reprints_url = "https://www.strictlybetter.eu/api/functional_reprints"
            response = requests.get(functional_reprints_url, timeout=6)
            response.raise_for_status()
            output_data = response.json()
            agent.send_output(
                agent_output_name='reprints_result',
                agent_result=output_data
            )
    except Exception as e:
        # All errors contained and serialized
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ObsoleteCardReprintFinder')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests

This agent is fully stateless, all outputs are serializable, and error handling is compliant with dora-rs agent interface requirements.
Call `run(agent)` from your orchestrator.
'''
