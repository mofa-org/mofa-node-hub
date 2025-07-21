from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    FIRST News public query agent. Fetches latest news from https://api.first.org/data/v1/news
    No input required. Uses HTTP GET. Returns result as a serializable dict.
    """
    # Facilitate other nodes to call this agent
    user_input = agent.receive_parameter('user_input')  # placeholder for dora-rs interface compliance

    news_url = 'https://api.first.org/data/v1/news'
    try:
        response = requests.get(news_url, timeout=10)
        response.raise_for_status()
        result = response.json()
    except Exception as e:
        # Contain all errors, return as output
        result = {'error': True, 'message': str(e)}
    
    # Output to dataflow -- ensure dict type
    agent.send_output(
        agent_output_name='first_news_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='FirstNewsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
