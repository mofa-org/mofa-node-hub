# Dependencies:
# - requests==2.31.0
#
# Description:
# Agent for accessing the Chinese Text Project's dictionary headwords via the public API.
# No input required, but a placeholder 'user_input' parameter is received to facilitate node connections.
# Outputs the list of dictionary headwords or error information.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

API_ENDPOINT = "https://api.ctext.org/getdictionaryheadwords"
TIMEOUT = 10  # seconds
MAX_RETRIES = 3
ENABLE_LOGGING = True

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate input port usage for downstream flow even if not required
        user_input = agent.receive_parameter('user_input')
        session = requests.Session()
        retries = 0
        while retries < MAX_RETRIES:
            try:
                if ENABLE_LOGGING:
                    print(f"[ChineseTextApiNode] GET {API_ENDPOINT}")
                response = session.get(API_ENDPOINT, timeout=TIMEOUT)
                if response.status_code == 200:
                    headwords = response.json()  # Assuming API returns JSON (check documentation if different)
                    agent.send_output(
                        agent_output_name='dictionary_headwords',
                        agent_result=headwords if isinstance(headwords, (dict, list)) else str(headwords)
                    )
                    return
                else:
                    if ENABLE_LOGGING:
                        print(f"[ChineseTextApiNode] Non-200 status code: {response.status_code}")
                    raise Exception(f"Non-200 status code: {response.status_code}")
            except Exception as e:
                retries += 1
                if ENABLE_LOGGING:
                    print(f"[ChineseTextApiNode] Attempt {retries} failed: {e}")
                if retries >= MAX_RETRIES:
                    agent.send_output(
                        agent_output_name='dictionary_headwords',
                        agent_result={
                            'error': True,
                            'message': str(e)
                        }
                    )
    except Exception as fatal_err:
        agent.send_output(
            agent_output_name='dictionary_headwords',
            agent_result={
                'error': True,
                'message': f"Fatal error: {str(fatal_err)}"
            }
        )

def main():
    agent = MofaAgent(agent_name='ChineseTextApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
