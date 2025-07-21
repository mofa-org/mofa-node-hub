# Dependencies: requests
# Make sure to include 'requests' in your requirements.txt:
# requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Dora-rs compatible agent for accessing Pollinations Free AI Text Generator.
    Outputs the AI's generated text as 'ai_text_output'.
    """
    # As this is a text generator endpoint with no input, facilitate upstream calling consistency
    user_input = agent.receive_parameter('user_input')  # "Dummy" input for dataflow consistency

    endpoint = "https://text.pollinations.ai/Hello"
    try:
        # GET request as per node configuration
        response = requests.get(endpoint, timeout=15)
        response.raise_for_status()
        ai_text = response.text  # assuming the service returns plain text output
    except Exception as err:
        agent.send_output(
            agent_output_name='ai_text_output',
            agent_result={
                "error": True,
                "error_msg": str(err)
            }
        )
        return

    # Output must be serializable, ensure string output
    agent.send_output(
        agent_output_name='ai_text_output',
        agent_result=str(ai_text)
    )

def main():
    agent = MofaAgent(agent_name='AIPollinationsTextNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
