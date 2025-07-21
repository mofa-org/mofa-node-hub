from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate inter-node calling: dummy user_input reception
    user_input = agent.receive_parameter('user_input')
    try:
        resp = requests.get('https://jokefather.com/api/jokes/random', timeout=10)
        resp.raise_for_status()
        data = resp.json()
        # Ensure serialization, pass only serializable output (dict or str)
        agent.send_output(
            agent_output_name='joke_response',
            agent_result=data
        )
    except Exception as e:
        error_message = {'error': True, 'message': str(e)}
        agent.send_output(
            agent_output_name='joke_response',
            agent_result=error_message
        )

def main():
    agent = MofaAgent(agent_name='JokeFatherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
