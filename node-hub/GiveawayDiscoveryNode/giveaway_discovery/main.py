from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No required input, but maintain dataflow compatibility
    user_input = agent.receive_parameter('user_input')
    endpoint = "https://gamerpower.com/api/giveaways"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        # Ensure output is serializable (list of dicts to list):
        agent.send_output(
            agent_output_name='giveaways',
            agent_result=data
        )
    except Exception as e:
        # Error handling: return error information
        agent.send_output(
            agent_output_name='giveaways',
            agent_result={'error': True, 'message': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='GiveawayDiscoveryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
