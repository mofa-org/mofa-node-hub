from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests
#   Install with: pip install requests

CHARACTER_ENDPOINT = "https://anapioficeandfire.com/api/characters/581"
HOUSE_ENDPOINT = "https://anapioficeandfire.com/api/houses/378"
TIMEOUT = 30       # seconds
RETRIES = 3        # Number of attempts on failure


def fetch_with_retries(url, max_retries=RETRIES, timeout=TIMEOUT):
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            if attempt == max_retries:
                # return error as string (serializable)
                return {"error": True, "msg": str(e), "endpoint": url}
            # Optionally, add sleep or backoff here if needed
        except Exception as e:
            # For non-request exceptions
            return {"error": True, "msg": str(e), "endpoint": url}
    # Fallback in case of a bug (should never reach here)
    return {"error": True, "msg": "Unknown failure", "endpoint": url}


@run_agent
def run(agent: MofaAgent):
    # Receive a dummy input to facilitate node chaining
    user_input = agent.receive_parameter('user_input')

    # Fetch character data
    character_data = fetch_with_retries(CHARACTER_ENDPOINT)
    agent.send_output(
        agent_output_name='character_details',
        agent_result=character_data
    )

    # Fetch house data
    house_data = fetch_with_retries(HOUSE_ENDPOINT)
    agent.send_output(
        agent_output_name='house_details',
        agent_result=house_data
    )

def main():
    agent = MofaAgent(agent_name='IceAndFireDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
