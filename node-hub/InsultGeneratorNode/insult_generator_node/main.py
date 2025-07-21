from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling for facilitating other nodes (stateless requirement)
        user_input = agent.receive_parameter('user_input')

        # Optionally allow external override for 'lang' and 'type', fallback to config defaults
        params = agent.receive_parameters(['lang', 'type'])
        lang = params.get('lang', 'en')
        resp_type = params.get('type', 'json')

        # Prepare API request
        endpoint = 'https://evilinsult.com/generate_insult.php'
        query_params = {
            'lang': lang,
            'type': resp_type
        }

        response = requests.get(endpoint, params=query_params, timeout=10)
        response.raise_for_status()

        # Parse and serialize output based on response type
        if resp_type == 'json':
            try:
                result = response.json()
            except Exception as parse_ex:
                agent.send_output(
                    agent_output_name='insult_error',
                    agent_result=f"Failed to parse JSON response: {parse_ex}"
                )
                return
        else:
            result = response.text
        agent.send_output(
            agent_output_name='insult',
            agent_result=result
        )
    except Exception as ex:
        # Contain all errors within the agent
        agent.send_output(
            agent_output_name='insult_error',
            agent_result=str(ex)
        )

def main():
    agent = MofaAgent(agent_name='InsultGeneratorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
