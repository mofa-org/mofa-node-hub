from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling (all agent input is string)
        digits = agent.receive_parameter('digits')
        # Environment variable for API key
        IIN_API_KEY = os.getenv('IIN_API_KEY')
        if not IIN_API_KEY:
            agent.send_output(
                agent_output_name='error',
                agent_result='API key not configured. Please set IIN_API_KEY in your .env.secret file.'
            )
            return
        # Prepare the API request
        endpoint = 'https://api.iinapi.com/iin'
        params = {
            'key': IIN_API_KEY,
            'digits': digits
        }
        try:
            response = requests.get(endpoint, params=params, timeout=10)
        except Exception as request_exc:
            agent.send_output(
                agent_output_name='error',
                agent_result=f'Network error occurred: {str(request_exc)}'
            )
            return
        if response.status_code != 200:
            agent.send_output(
                agent_output_name='error',
                agent_result=f'API returned HTTP {response.status_code}: {response.text}'
            )
            return
        try:
            api_data = response.json()
        except Exception as json_exc:
            agent.send_output(
                agent_output_name='error',
                agent_result=f'Failed to parse API JSON: {str(json_exc)}'
            )
            return
        # Output metadata (must be serializable)
        agent.send_output(
            agent_output_name='card_metadata',
            agent_result=api_data if isinstance(api_data, (dict, list, str)) else str(api_data)
        )
    except Exception as exc:
        agent.send_output(
            agent_output_name='error',
            agent_result=f'Unhandled error: {str(exc)}'
        )

def main():
    agent = MofaAgent(agent_name='CardMetadataResolverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

.env.secret configuration required:
IIN_API_KEY=your_iin_api_key_here
"""