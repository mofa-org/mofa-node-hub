# Dependencies: requests (install via pip if needed)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input port for dataflow even if no input is needed
    user_input = agent.receive_parameter('user_input')
    # Endpoint configuration
    API_ENDPOINT = "https://api.elifesciences.org/articles"
    try:
        response = requests.get(API_ENDPOINT, timeout=12)
        response.raise_for_status()
        # Response JSON is serializable
        articles = response.json()
        agent.send_output(
            agent_output_name='article_list',
            agent_result=articles
        )
    except requests.RequestException as e:
        # Return error as string for serialization
        agent.send_output(
            agent_output_name='article_list',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ArticleListRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
