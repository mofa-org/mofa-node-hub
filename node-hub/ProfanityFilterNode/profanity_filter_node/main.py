from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    # Receives input (string to be checked for profanity)
    input_text = agent.receive_parameter('input_text')
    try:
        if not isinstance(input_text, str):
            raise ValueError("Input must be a string.")

        # Preparing the purgomalum API
        api_url = "https://www.purgomalum.com/service/json"
        params = {'text': input_text}
        response = requests.get(api_url, params=params, timeout=10)

        # Check for HTTP errors
        response.raise_for_status()
        try:
            result = response.json()
        except Exception:
            raise ValueError("Received non-JSON response from API.")

        # Validate API response structure
        if 'result' not in result:
            raise ValueError("Unexpected API response structure: {}".format(result))

        censored_text = result['result']
        # Output via framework: output_port is 'filtered_text'
        agent.send_output(
            agent_output_name='filtered_text',
            agent_result=str(censored_text)
        )

    except Exception as e:
        error_message = {
            'error': True,
            'details': str(e)
        }
        agent.send_output(
            agent_output_name='filtered_text',
            agent_result=json.dumps(error_message)
        )

def main():
    agent = MofaAgent(agent_name='ProfanityFilterNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
