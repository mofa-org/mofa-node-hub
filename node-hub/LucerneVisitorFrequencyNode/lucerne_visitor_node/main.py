# Dependencies: requests, python-dotenv
# Place your API key in a .env.secret file as: API_KEY=your_api_key_here

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os
from dotenv import load_dotenv

@run_agent
def run(agent: MofaAgent):
    # Accept input to facilitate framework orchestration, even if unused
    user_input = agent.receive_parameter('user_input')

    # Load API Key safely from environment
    try:
        load_dotenv('.env.secret')
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError('API_KEY not found in environment.')
    except Exception as e:
        agent.send_output(
            agent_output_name='visitor_data',
            agent_result={'error': f'Failed to load API key: {str(e)}'}
        )
        return

    # API endpoint
    endpoint = 'https://portal.alfons.io/app/devicecounter/api/sensors'
    params = {'api_key': api_key}
    try:
        response = requests.get(endpoint, params=params, timeout=15)
        response.raise_for_status()
        # Ensure serializable result
        try:
            data = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='visitor_data',
                agent_result={'error': f'Failed to parse JSON: {str(e)}'}
            )
            return
        agent.send_output(
            agent_output_name='visitor_data',
            agent_result=data if isinstance(data, (dict, list)) else str(data)
        )
    except requests.RequestException as e:
        agent.send_output(
            agent_output_name='visitor_data',
            agent_result={'error': f'API request failed: {str(e)}'}
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='visitor_data',
            agent_result={'error': f'Unexpected error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='LucerneVisitorFrequencyNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
