from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    try:
        # Accept a user_agent parameter (String, required by API)
        user_agent = agent.receive_parameter('user_agent')
        if not user_agent or not isinstance(user_agent, str):
            raise ValueError("Parameter 'user_agent' is required and must be a string.")

        # Endpoint from config or default
        endpoint = "https://api.apicagent.com/"

        # Build GET request URL (The API expects user agent in query param 'ua')
        request_url = f"{endpoint}?ua={requests.utils.quote(user_agent)}"
        headers = {
            'Accept': 'application/json'
        }
        response = requests.get(request_url, headers=headers, timeout=10)
        response.raise_for_status()
        parsed = response.json()

        # Serialize response (dict)
        agent.send_output(
            agent_output_name='user_agent_info',
            agent_result=parsed
        )
    except Exception as e:
        # Error handling, return as serialization-friendly dict
        agent.send_output(
            agent_output_name='user_agent_info',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='UserAgentDetectionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests
'''
