# Dependencies required: requests
# Ensure the following in requirements.txt:
# requests>=2.25.1

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # To facilitate dataflow integration, allow receiving a user_input parameter (even if unused directly)
        user_input = agent.receive_parameter('user_input')
        
        # Step 1: Find MBID from MusicBrainz for Billie Jean by Michael Jackson
        mb_search_url = "https://musicbrainz.org/ws/2/recording/?query=recording:%22Billie%20Jean%22+AND+artist:%22Michael%20Jackson%22&fmt=json"
        mb_response = requests.get(mb_search_url, timeout=10)
        mb_response.raise_for_status()
        mb_data = mb_response.json()
        
        # Extract MBID (MusicBrainz Recording ID)
        mbid = None
        if 'recordings' in mb_data and len(mb_data['recordings']) > 0:
            mbid = mb_data['recordings'][0].get('id')
        if not mbid:
            agent.send_output(
                agent_output_name='error',
                agent_result='No valid MBID found for Billie Jean by Michael Jackson.'
            )
            return
        
        # Step 2: Query AcousticBrainz APIs for low-level and high-level data
        url_low = f"https://acousticbrainz.org/{mbid}/low-level"
        url_high = f"https://acousticbrainz.org/{mbid}/high-level"

        low_level_data, high_level_data = None, None
        # Fetch low-level data
        try:
            resp_low = requests.get(url_low, timeout=10)
            resp_low.raise_for_status()
            low_level_data = resp_low.json()
        except Exception as e:
            low_level_data = {'error': f'Unable to retrieve low-level data: {str(e)}'}
        # Fetch high-level data
        try:
            resp_high = requests.get(url_high, timeout=10)
            resp_high.raise_for_status()
            high_level_data = resp_high.json()
        except Exception as e:
            high_level_data = {'error': f'Unable to retrieve high-level data: {str(e)}'}

        # Aggregate and output result
        result = {
            'recording_mbid': mbid,
            'musicbrainz_summary': mb_data['recordings'][0],
            'acousticbrainz_low_level': low_level_data,
            'acousticbrainz_high_level': high_level_data
        }
        agent.send_output(
            agent_output_name='music_data',
            agent_result=result
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='error',
            agent_result={
                'error': str(ex)
            }
        )

def main():
    agent = MofaAgent(agent_name='MusicDataNodeBuilder')
    run(agent=agent)

if __name__ == '__main__':
    main()
