from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes even if not strictly required
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('http://numbersapi.com/random/math?json', timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure response is serializable
        agent.send_output(
            agent_output_name='fact',
            agent_result=data
        )
    except Exception as e:
        # Ensure no uncaught exceptions propagate out
        agent.send_output(
            agent_output_name='fact',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='NumbersFactsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
# Ensure to add 'requests' to your requirements.
