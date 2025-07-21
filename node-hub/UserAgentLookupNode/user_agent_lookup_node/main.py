from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling: expect 'ua' parameter as user agent string
        ua = agent.receive_parameter('ua')
        if not isinstance(ua, str):
            raise ValueError("Parameter 'ua' must be a string.")
        # Prepare API request
        endpoint = 'https://www.useragentlookup.com/api/user-agent'
        params = {'ua': ua}
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError if status != 200
        try:
            result = response.json()
        except Exception:
            # If response is not JSON serializable
            result = {'error': 'Non-JSON response received from API.', 'content': response.text}
    except Exception as e:
        # Error containment and serialization validation
        result = {'error': str(e)}
    agent.send_output(
        agent_output_name='user_agent_parsed',
        agent_result=result  # Ensure dict is serializable
    )

def main():
    agent = MofaAgent(agent_name='UserAgentLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
#
# Dataflow Ports:
# Input:  ua (user agent string)
# Output: user_agent_parsed (parsed info as dict or error response)