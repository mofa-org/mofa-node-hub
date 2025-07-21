from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate call by other nodes
        user_input = agent.receive_parameter('user_input')

        # Receive input: ua (user agent string), else use default
        ua = agent.receive_parameter('ua')
        if not ua or not isinstance(ua, str) or ua.strip() == "":
            # Support for default from config
            ua = os.getenv("DEFAULT_USER_AGENT", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")

        # Retrieve API key from env (should be set in .env.secret)
        api_key = os.getenv("USERAGENT_APP_KEY")
        if not api_key:
            raise RuntimeError("USERAGENT_APP_KEY not set in environment")

        endpoint = os.getenv("USERAGENT_API_ENDPOINT", "https://api.useragent.app/parse")

        # Compose request
        params = {
            'key': api_key,
            'ua': ua
        }
        response = requests.get(endpoint, params=params, timeout=30)
        response.raise_for_status()
        result = response.json()

        # Ensure serialization
        agent.send_output(
            agent_output_name='parsed_user_agent',
            agent_result=result
        )
    except Exception as e:
        # Contain error and send as serializable string
        agent.send_output(
            agent_output_name='parsed_user_agent',
            agent_result={
                'error': True,
                'error_msg': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='UserAgentParserNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
