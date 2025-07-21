from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive the 'text' parameter as string. Facilitate DAG chaining even if empty input.
        user_input = agent.receive_parameter('text')
        if user_input is None or user_input.strip() == '':
            user_input = "hello world"  # Use default if not provided

        # API endpoint details
        endpoint = "https://api.funtranslations.com/translate/morse.json"
        params = {'text': user_input}
        headers = {
            'Accept': 'application/json'
        }

        # Send GET request
        response = requests.get(endpoint, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        api_result = response.json()  # Should be serializable

        # Deliver output through dataflow port
        agent.send_output(
            agent_output_name='morse_code_translation',
            agent_result=api_result
        )
    except Exception as e:
        error_message = f"Error during Morse code translation: {str(e)}"
        agent.send_output(
            agent_output_name='morse_code_translation',
            agent_result={'error': error_message}
        )

def main():
    agent = MofaAgent(agent_name='MorseCodeTranslator')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# This Agent consumes input on the 'text' port and outputs the API response (or error) on 'morse_code_translation'.