from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
from typing import Dict, Any

# Documented dependencies:
# - requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent to fetch the latest Red Tide Situation updates from the Hong Kong AFCD data portal in different languages.
    Input: 'language' string: one of 'traditional', 'simplified', 'english'.
    Output: JSON dict containing results from the selected endpoint, delivered via 'red_tide_data' port.
    """
    try:
        input_params = agent.receive_parameter('language')  # string type input
        language = str(input_params).strip().lower()
    except Exception as e:
        agent.send_output(
            agent_output_name='red_tide_data',
            agent_result={
                'error': f'Failed to receive input parameter: {str(e)}'
            }
        )
        return

    ENDPOINTS = {
        'traditional': {
            'url': 'https://redtide.afcd.gov.hk/data/RTMS_ob_RTLC.json',
            'description': 'Update of Red Tide Situation (Traditional Chinese)'
        },
        'simplified': {
            'url': 'https://redtide.afcd.gov.hk/data/RTMS_ob_RTLS.json',
            'description': 'Update of Red Tide Situation (Simplified Chinese)'
        },
        'english': {
            'url': 'https://redtide.afcd.gov.hk/data/RTMS_ob_RTLE.json',
            'description': 'Update of Red Tide Situation (English)'
        }
    }

    # Validate language
    if language not in ENDPOINTS:
        agent.send_output(
            agent_output_name='red_tide_data',
            agent_result={
                'error': f"Invalid language parameter: {language}. Expected one of: traditional, simplified, english."
            }
        )
        return

    endpoint_info = ENDPOINTS[language]
    url = endpoint_info['url']
    description = endpoint_info['description']
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()  # assuming proper JSON is returned
        output_data = {
            'description': description,
            'source_url': url,
            'data': data
        }
    except Exception as e:
        output_data = {
            'error': f'Failed to fetch or decode data from {url}: {str(e)}'
        }
    agent.send_output(
        agent_output_name='red_tide_data',
        agent_result=output_data
    )

def main():
    agent = MofaAgent(agent_name='RedTideSituationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
