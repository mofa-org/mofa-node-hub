"""
Agent Name: AffirmationStatementNode
Module Name: affirmation_node
Description: Fetches a random inspirational affirmation from the affirmations.dev API, returning it via the specified agent output port.

Requirements:
- Requires 'requests' library: install via `pip install requests`
- No input required, but to comply with dora-rs agent interface, receive the (unused) parameter 'user_input'.
"""
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

AFFIRMATION_ENDPOINT = "https://www.affirmations.dev/"
DEFAULT_TIMEOUT = 10  # seconds

@run_agent
def run(agent: MofaAgent):
    # To support chaining with other nodes, we receive (but do not use) a dummy input
    user_input = agent.receive_parameter('user_input')  # Required for interface compliance
    try:
        response = requests.get(AFFIRMATION_ENDPOINT, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        # Validate API format
        affirmation = data.get('affirmation')
        if not isinstance(affirmation, str):
            raise ValueError("API response malformed: missing 'affirmation' string")
        # Output as a dictionary (ensures serializability and extensibility)
        agent.send_output(
            agent_output_name='affirmation',
            agent_result={'affirmation': affirmation}
        )
    except Exception as e:
        # Graceful error reporting through output port
        agent.send_output(
            agent_output_name='affirmation',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='AffirmationStatementNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
