# Dependencies:
#   requests
#
# Node functionality: Provides API data from Dog CEO API endpoints.
# All dora-rs standards strictly enforced.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
from requests.adapters import HTTPAdapter, Retry

BASE_URL = "https://dog.ceo/api"
TIMEOUT_S = 30
RETRY_ATTEMPTS = 3

API_ENDPOINTS = {
    'all_breeds': f"{BASE_URL}/breeds/list/all",
    'random_image': f"{BASE_URL}/breeds/image/random",
    'affenpinscher_image': f"{BASE_URL}/breed/affenpinscher/images/random",
}

@run_agent
def run(agent: MofaAgent):
    # Accept an operation parameter to choose action
    user_input = agent.receive_parameter('user_input')  # Accept operation input for orchestration
    try:
        operation = str(user_input).strip().lower() if user_input else ''

        session = requests.Session()
        retries = Retry(total=RETRY_ATTEMPTS, backoff_factor=1,
                        status_forcelist=[502, 503, 504])
        session.mount('https://', HTTPAdapter(max_retries=retries))

        if operation == 'list_breeds':
            resp = session.get(API_ENDPOINTS['all_breeds'], timeout=TIMEOUT_S)
            resp.raise_for_status()
            agent.send_output(
                agent_output_name='breeds_list',
                agent_result=resp.json()  # dict serializable
            )
        elif operation == 'random_image':
            resp = session.get(API_ENDPOINTS['random_image'], timeout=TIMEOUT_S)
            resp.raise_for_status()
            agent.send_output(
                agent_output_name='random_dog_image',
                agent_result=resp.json()
            )
        elif operation == 'affenpinscher_image':
            resp = session.get(API_ENDPOINTS['affenpinscher_image'], timeout=TIMEOUT_S)
            resp.raise_for_status()
            agent.send_output(
                agent_output_name='affenpinscher_image',
                agent_result=resp.json()
            )
        else:
            agent.send_output(
                agent_output_name='error',
                agent_result={
                    "error": "Invalid operation. Supported: list_breeds, random_image, affenpinscher_image."
                }
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='DogApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
