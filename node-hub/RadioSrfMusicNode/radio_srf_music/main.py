from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No input required, but for compatibility, receive a dummy string parameter
    user_input = agent.receive_parameter('user_input')  # Allows easy chaining in pipeline
    api_url = "https://il.srgssr.ch/integrationlayer/2.0/srf/songList/radio/byChannel/69e8ac16-4327-4af4-b873-fd5cd6e895a7"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Optionally extract only relevant info (e.g. song title, artist) for clarity
        song_list = []
        for song in data.get('playlist', []):
            song_info = {
                'title': song.get('title'),
                'artist': song.get('interpreten'),
                'start': song.get('start'),
                'end': song.get('end')
            }
            song_list.append(song_info)
        agent.send_output(
            agent_output_name='radio_srf_1_song_list',
            agent_result=song_list  # List of dicts is JSON-serializable
        )
    except Exception as e:
        # Return error as output for traceability
        agent.send_output(
            agent_output_name='radio_srf_1_song_list',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='RadioSrfMusicNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
