from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate downstream calls even though not used
    user_input = agent.receive_parameter('user_input')
    try:
        url = 'https://api.kanye.rest/'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure output is serializable
        agent.send_output(
            agent_output_name='kanye_quote',
            agent_result=data.get('quote', '')
        )
    except requests.RequestException as e:
        agent.send_output(
            agent_output_name='kanye_quote',
            agent_result=f"Error fetching Kanye quote: {str(e)}"
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='kanye_quote',
            agent_result=f"Unexpected error: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='KanyeQuotesNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests