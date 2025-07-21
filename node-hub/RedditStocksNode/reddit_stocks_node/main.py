from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Add a receive_parameter call for dataflow compatibility
    user_input = agent.receive_parameter('user_input')
    # The node does not require any input, so user_input can be ignored

    api_url = "https://tradestie.com/api/v1/apps/reddit"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # Attempt to handle non-seriazable objects
        try:
            stocks_data = response.json()
        except Exception as e:
            stocks_data = response.text  # fallback to raw text
        # Always return serializable (usually dict/list)
        agent.send_output(
            agent_output_name='reddit_stocks',
            agent_result=stocks_data
        )
    except Exception as err:
        # Error handling; output as string for serialization
        agent.send_output(
            agent_output_name='reddit_stocks',
            agent_result={'error': str(err)}
        )

def main():
    agent = MofaAgent(agent_name='RedditStocksNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   - requests (ensure in agent requirements)
# Documentation:
#   Uses the public Reddit Stocks API with no required authentication.
#   No input required (placeholder input for node connection).