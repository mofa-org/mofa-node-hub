from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling: accept 'user_input' for API query, fallback to default if not provided
        user_input = agent.receive_parameter('user_input')
        if not user_input or user_input.strip() == '':
            api_text = os.getenv('DEFAULT_TEXT', 'iPhone')  # fallback default
        else:
            api_text = user_input.strip()

        # Endpoint from config/env
        api_endpoint = os.getenv('API_ENDPOINT', 'https://abhi-api.vercel.app/api/search/ringtone')
        request_url = f"{api_endpoint}?text={api_text}"

        # Make GET request
        response = requests.get(request_url, timeout=10)
        try:
            response.raise_for_status()
            result = response.json()
        except Exception as e:
            result = {'error': 'Failed to process API response', 'details': str(e)}

        # Ensure output is serializable
        agent.send_output(
            agent_output_name='api_response',
            agent_result=result
        )
    except Exception as err:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={'error': 'Unhandled exception.', 'details': str(err)}
        )

def main():
    agent = MofaAgent(agent_name='RingtoneSearchNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests

Environment Variables (.env.secret) supported:
- API_ENDPOINT: Override endpoint if needed.
- DEFAULT_TEXT: Default query string if input missing.
'''
