from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input URL from the appropriate dataflow port
        target_url = agent.receive_parameter('target_url')  # All input as string

        # Ensure the input is a non-empty string
        if not isinstance(target_url, str) or not target_url.strip():
            agent.send_output(
                agent_output_name='metadata_output',
                agent_result={'error': 'Input target_url must be a non-empty string.'}
            )
            return

        # Microlink API endpoint and parameter key
        MICROLINK_ENDPOINT = "https://api.microlink.io/"
        PARAM_NAME = "url"
        # Assemble complete request URL and parameters
        params = {PARAM_NAME: target_url.strip()}

        response = requests.get(MICROLINK_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()
        metadata = response.json()
        # Validate that JSON is serializable and not too large
        agent.send_output(
            agent_output_name='metadata_output',
            agent_result=metadata
        )
    except Exception as e:
        # Catch all exceptions and send as error output
        agent.send_output(
            agent_output_name='metadata_output',
            agent_result={
                'error': f'Exception occurred during metadata retrieval: {str(e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='PageMetadataRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests (install with `pip install requests`)
# Dataflow Ports:
#   Input: target_url (str)
#   Output: metadata_output (dict or error dict)
# All HTTP request parameters are string type, and outputs are serializable.