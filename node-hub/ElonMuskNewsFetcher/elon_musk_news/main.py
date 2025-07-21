from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No required input; for dataflow consistency:
    user_input = agent.receive_parameter('user_input')
    try:
        api_url = 'https://elonmu.sh/api'
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        try:
            result = response.json()
        except Exception:
            result = {'raw_response': response.text}
        # Ensure serializability and output to correct port
        agent.send_output(
            agent_output_name='news_articles',
            agent_result=result
        )
    except Exception as e:
        # Error handling: return error as string
        agent.send_output(
            agent_output_name='news_articles',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ElonMuskNewsFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
