from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate input for potential future expansions
        user_input = agent.receive_parameter('user_input')
        # This agent fetches the definition of 'fart' only; endpoint is hardcoded
        endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/fart"
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            # DictionaryAPI always returns list at top level
            agent.send_output(
                agent_output_name='definition_data',
                agent_result=data
            )
        else:
            # Non-200 response handling
            agent.send_output(
                agent_output_name='definition_data',
                agent_result={
                    'error': f'API returned status code {response.status_code}',
                    'response': response.text
                }
            )
    except Exception as e:
        # Complete error containment
        agent.send_output(
            agent_output_name='definition_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='DictionaryDefinitionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# This agent uses 'requests' for HTTP requests. Ensure installation via 'pip install requests'.
# All inputs and outputs are handled via the dora-rs compliance interface, stateless design, and errors are fully contained within the agent boundaries.