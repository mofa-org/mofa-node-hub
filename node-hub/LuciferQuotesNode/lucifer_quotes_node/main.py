from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate calls from other nodes even if no input is needed
        user_input = agent.receive_parameter('user_input')

        response = requests.get('https://lucifer-quotes.vercel.app/api/quotes', timeout=10)
        response.raise_for_status()
        data = response.json()  # The API returns JSON

        # Ensure data is serializable (already a dict or list)
        agent.send_output(
            agent_output_name='lucifer_quote',
            agent_result=data
        )
    except Exception as e:
        # Graceful error handling: provide error details in output
        agent.send_output(
            agent_output_name='lucifer_quote',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='LuciferQuotesNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
