from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Hypixel Skyblock Bazaar Node: Fetches bazaar information from the official Hypixel API.
    API Documentation: https://api.hypixel.net/?ref=freepublicapis.com
    Output dataflow port: 'bazaar_data'
    """
    # Sentence to facilitate calling from other nodes (no input required)
    user_input = agent.receive_parameter('user_input')

    api_url = "https://api.hypixel.net/skyblock/bazaar"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        result = response.json()
        # Ensure output is serializable (dict type is acceptable)
        agent.send_output(
            agent_output_name='bazaar_data',
            agent_result=result
        )
    except requests.RequestException as e:
        error_msg = f"Error fetching Hypixel Bazaar API: {str(e)}"
        agent.send_output(
            agent_output_name='bazaar_data',
            agent_result={"error": error_msg}
        )
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        agent.send_output(
            agent_output_name='bazaar_data',
            agent_result={"error": error_msg}
        )

def main():
    agent = MofaAgent(agent_name='HypixelSkyblockBazaarNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests
  Install with: pip install requests
"""