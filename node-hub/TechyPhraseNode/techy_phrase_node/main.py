from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No required input, but add a receive_parameter for compatibility
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://techy-api.vercel.app/api/json', timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure the output is serializable, only send relevant part if present
        agent.send_output(
            agent_output_name='techy_phrase',
            agent_result=data if isinstance(data, (dict, list, str)) else str(data)
        )
    except Exception as e:
        error_message = f"Error fetching techy phrase: {str(e)}"
        agent.send_output(
            agent_output_name='techy_phrase',
            agent_result={'error': error_message}
        )

def main():
    agent = MofaAgent(agent_name='TechyPhraseNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
