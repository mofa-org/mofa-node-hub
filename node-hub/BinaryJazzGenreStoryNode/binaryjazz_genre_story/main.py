from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # This agent does not require meaningful input, but to facilitate orchestration,
    # we receive 'user_input' for dataflow consistency.
    user_input = agent.receive_parameter('user_input')
    try:
        genre_resp = requests.get(
            'https://binaryjazz.us/wp-json/genrenator/v1/genre/5', timeout=10
        )
        genre_resp.raise_for_status()
        genre_data = genre_resp.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='genre_result',
            agent_result={
                'error': f'Failed to fetch genre: {str(e)}'
            }
        )
        genre_data = None

    try:
        story_resp = requests.get(
            'https://binaryjazz.us/wp-json/genrenator/v1/story/5', timeout=10
        )
        story_resp.raise_for_status()
        story_data = story_resp.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='story_result',
            agent_result={
                'error': f'Failed to fetch story: {str(e)}'
            }
        )
        story_data = None

    # Result output: Use valid data, else send error dict
    if genre_data is not None:
        agent.send_output(
            agent_output_name='genre_result',
            agent_result=genre_data
        )
    if story_data is not None:
        agent.send_output(
            agent_output_name='story_result',
            agent_result=story_data
        )

def main():
    agent = MofaAgent(agent_name='BinaryJazzGenreStoryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests >=2.0.0

This agent fetches genre and story data from the BinaryJazz API. It exposes two output ports:
- 'genre_result': Outputs the genre JSON or an error dict.
- 'story_result': Outputs the story JSON or an error dict.

No user configuration or authentication is required.
"""