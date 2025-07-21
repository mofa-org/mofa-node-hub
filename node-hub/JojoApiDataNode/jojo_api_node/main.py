from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Placeholder to facilitate other nodes to call this agent
    user_input = agent.receive_parameter('user_input')

    try:
        # Fetch characters data
        characters_response = requests.get('https://stand-by-me.herokuapp.com/api/v1/characters', timeout=10)
        characters_response.raise_for_status()
        characters_data = characters_response.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='characters',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )
        characters_data = None

    try:
        # Fetch stands data
        stands_response = requests.get('https://stand-by-me.herokuapp.com/api/v1/stands', timeout=10)
        stands_response.raise_for_status()
        stands_data = stands_response.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='stands',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )
        stands_data = None

    # Only send data if no error occurred
    if characters_data is not None:
        agent.send_output(
            agent_output_name='characters',
            agent_result=characters_data
        )
    if stands_data is not None:
        agent.send_output(
            agent_output_name='stands',
            agent_result=stands_data
        )

def main():
    agent = MofaAgent(agent_name='JojoApiDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests

Output Ports:
- 'characters' : returns the characters data as JSON-serializable dict/list
- 'stands'     : returns the stands data as JSON-serializable dict/list
'''
