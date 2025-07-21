from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent for providing logo resources via logotypes.dev API.
    Receives an input parameter: 'action' (str) - 'all' or 'random'
    - 'all': fetch all logos
    - 'random': fetch a random logo
    """
    try:
        # Expecting action as a string: 'all' or 'random'
        action = agent.receive_parameter('action')
        if not isinstance(action, str):
            raise ValueError("Input parameter 'action' must be a string.")

        # Configurable endpoints (could be loaded from env/yaml if required)
        ALL_LOGOS_URL = "https://logotypes.dev/all"
        RANDOM_LOGO_URL = "https://logotypes.dev/random/data"
        TIMEOUT = 10  # seconds

        if action.strip().lower() == 'all':
            response = requests.get(ALL_LOGOS_URL, timeout=TIMEOUT)
            response.raise_for_status()
            data = response.json()
            output_port = 'all_logos'
        elif action.strip().lower() == 'random':
            response = requests.get(RANDOM_LOGO_URL, timeout=TIMEOUT)
            response.raise_for_status()
            data = response.json()
            output_port = 'random_logo'
        else:
            raise ValueError(f"Invalid action: {action}. Expected 'all' or 'random'.")

        # Ensure output is serializable (usually list or dict)
        agent.send_output(
            agent_output_name=output_port,
            agent_result=data
        )
    except Exception as e:
        # Serialize the error for framework handling
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='LogoProviderNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
