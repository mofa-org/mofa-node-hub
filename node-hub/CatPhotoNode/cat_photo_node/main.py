# Dependencies: requests
# Ensure 'requests' is listed in requirements.txt or pip-installed in your deployment environment

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    CatPhotoNode Agent
    - GET a random cat photo from https://purr.woody.cat
    - Outputs the photo data as JSON (keys: 'url', 'status_code') or error message
    - Stateless and robust error handling
    """
    # Receive input (to facilitate graph triggering even when no specific input needed)
    user_input = agent.receive_parameter('user_input')

    endpoint = "https://purr.woody.cat"  # Get random photo endpoint
    output_dict = {}
    try:
        resp = requests.get(endpoint, timeout=15)
        resp.raise_for_status()

        output_dict = {
            'url': resp.url,
            'status_code': resp.status_code
        }
    except Exception as e:
        output_dict = {
            'error': str(e)
        }
    
    # Output JSON-serializable result on 'cat_photo' port
    agent.send_output(
        agent_output_name='cat_photo',
        agent_result=output_dict
    )

def main():
    agent = MofaAgent(agent_name='CatPhotoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
