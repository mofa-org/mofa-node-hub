from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Fetches data on Nutella from OpenFoodFacts API.
    This agent has no external input ports but expects to be invoked in the pipeline.
    """
    # To facilitate other nodes to call this one
    user_input = agent.receive_parameter('user_input')

    try:
        response = requests.get('https://world.openfoodfacts.org/api/v0/product/3017620422003.json', timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception as json_exc:
            # If JSON decoding fails
            agent.send_output(
                agent_output_name='api_output',
                agent_result={
                    "error": "Failed to decode JSON response",
                    "details": str(json_exc)
                }
            )
            return
        # Serialization test: ensure output is a dict
        agent.send_output(
            agent_output_name='api_output',
            agent_result=data    # dict is serializable
        )
    except Exception as exc:
        agent.send_output(
            agent_output_name='api_output',
            agent_result={
                "error": "Failed to call OpenFoodFacts API",
                "details": str(exc)
            }
        )

def main():
    agent = MofaAgent(agent_name='OpenFoodFactsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# Make sure to install requests: pip install requests