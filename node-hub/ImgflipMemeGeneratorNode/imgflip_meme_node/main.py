from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes calling this, even though no parameter is required
    user_input = agent.receive_parameter('user_input')

    api_url = "https://api.imgflip.com/get_memes"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        json_result = response.json()
        # Validate serialization
        if not isinstance(json_result, dict):
            raise ValueError("API response is not dict serializable.")
        agent.send_output(
            agent_output_name='memes_api_response',
            agent_result=json_result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='memes_api_response',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ImgflipMemeGeneratorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   - requests
# This agent does not require any input but includes a dummy receive_parameter for framework compatibility.
# All error handling is strictly internal; outputs are always serializable (dict).
# Dataflow port for output: 'memes_api_response'