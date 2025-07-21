from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate calls by other nodes by expecting a dummy input (even if not used)
    user_input = agent.receive_parameter('user_input')

    # Endpoint information
    api_url = "https://html-creator.en.uptodown.com/android"

    try:
        # As per configuration, no parameters are specified; simple GET request
        response = requests.get(api_url)
        response.raise_for_status()
        try:
            # Try to parse HTML as text to ensure serialization
            data = response.text
        except Exception as parse_err:
            agent.send_output("api_error", {"error": f"Failed to parse response: {str(parse_err)}"})
            return
        agent.send_output(
            agent_output_name="html_page",
            agent_result=data  # HTML is text, hence serializable
        )
    except Exception as e:
        agent.send_output(
            agent_output_name="api_error",
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='HtmlCreatorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
