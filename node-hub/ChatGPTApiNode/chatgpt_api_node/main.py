from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive input from dataflow (always str)
    try:
        user_input = agent.receive_parameter('user_input')  # Facilitates upstream node calling
        if not isinstance(user_input, str):
            user_input = str(user_input)
        # API endpoint from config
        api_endpoint = "https://api.apitools.workers.dev/api/ai/chatgpt4"
        # Prepare GET parameters (API uses ?text=...)
        params = {'text': user_input}
        response = requests.get(api_endpoint, params=params, timeout=20)
        response.raise_for_status()
        # The API responds with JSON; ensure we only send string/dict/list
        try:
            output_data = response.json()
        except Exception:
            output_data = response.text
        # Output to the dataflow port
        agent.send_output(
            agent_output_name='chatgpt4_response',
            agent_result=output_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='chatgpt4_response',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ChatGPTApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
# Dependencies:
# - requests
#
# Ports:
# Input:   'user_input'    (str)
# Output:  'chatgpt4_response' (dict/str, serializable)
#
# All error handling is contained. Stateless. Dataflows/ports properly named.
# Configure the endpoint/keys via config args or .env if needed (none required here).
"""