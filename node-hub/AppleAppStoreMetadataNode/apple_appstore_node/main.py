from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # As no direct input is required, provide compatibility input
    user_input = agent.receive_parameter('user_input')
    try:
        endpoint = "https://app-store-metadata-api.kula.app/api/v1/apple/apps/361309726"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Ensure serializability
        data = response.json()
        agent.send_output(
            agent_output_name='appstore_metadata',
            agent_result=data
        )
    except Exception as e:
        # Error handling and serialization
        agent.send_output(
            agent_output_name='appstore_metadata',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='AppleAppStoreMetadataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests

Install via: pip install requests
'''
