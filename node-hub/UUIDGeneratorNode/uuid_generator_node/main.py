# Dependencies: requests
# Make sure to install requests in your environment: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate dataflow even if caller does not provide input
        user_input = agent.receive_parameter('user_input')
        # Try to get 'count' from input, else default to 3 as per config/yml
        count_param = agent.receive_parameter('count')
        try:
            count = int(count_param)
        except (ValueError, TypeError):
            count = 3  # default as per yml_config
        # Build endpoint URL
        endpoint = f"https://www.uuidtools.com/api/generate/v1/count/{count}"
        response = requests.get(endpoint, timeout=10)
        if response.status_code != 200:
            result = {'error': f'API returned status {response.status_code}', 'response_text': response.text}
        else:
            try:
                uuids = response.json()  # API returns a JSON array of UUIDs
                # Ensure that output is serializable and expected type
                result = {'uuids': uuids, 'count': len(uuids)}
            except Exception as ex:
                result = {'error': 'Failed to parse API response as JSON', 'exception': str(ex)}
    except Exception as e:
        result = {'error': 'UUID generation failed', 'exception': str(e)}
    # Output delivery, always serializable
    agent.send_output(
        agent_output_name='uuid_list',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='UUIDGeneratorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
