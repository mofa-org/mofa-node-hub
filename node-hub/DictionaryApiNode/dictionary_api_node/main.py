from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Even though the API does not require parameters, to facilitate downstream calls:
    user_input = agent.receive_parameter('user_input')  # For compatibility with dora-rs dataflow nodes

    url = 'https://freedictionaryapi.com/api/v1/entries/en/public'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='dictionary_api_result',
                agent_result={'error': 'Invalid JSON response', 'details': str(e)}
            )
            return
        agent.send_output(
            agent_output_name='dictionary_api_result',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='dictionary_api_result',
            agent_result={'error': 'Request failed', 'details': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='DictionaryApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
