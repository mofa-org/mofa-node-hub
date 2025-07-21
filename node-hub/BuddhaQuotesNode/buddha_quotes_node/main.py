from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input presence for composition, though none is needed for API call
    user_input = agent.receive_parameter('user_input')  # Allows other nodes to call this node easily
    api_url = "https://buddha-api.com/api/random"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Ensure output is serializable
        if not isinstance(data, (dict, list, str)):
            processed_data = str(data)
        else:
            processed_data = data
        agent.send_output(
            agent_output_name='buddha_quote',
            agent_result=processed_data
        )
    except Exception as e:
        # Handle all errors and output a clear message
        agent.send_output(
            agent_output_name='buddha_quote',
            agent_result={
                'error': 'Failed to fetch Buddha quote',
                'detail': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='BuddhaQuotesNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
# Ensure package 'requests' is included in your Python environment.