from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Ensures compatibility with dora-rs: allow user_input as dummy parameter for dataflow integrity
    user_input = agent.receive_parameter('user_input')
    try:
        # No additional parameters required by the API
        endpoint = "http://answerbook.david888.com/?lang=en"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        advice = response.text  # The API returns a plain text string

        # Ensure the output is a string
        agent.send_output(
            agent_output_name='book_of_answers_response',
            agent_result=str(advice)
        )
    except Exception as e:
        # Capture error and send as output (for graceful dataflow failure handling)
        agent.send_output(
            agent_output_name='book_of_answers_response',
            agent_result=f"Error: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='BookOfAnswersNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
