from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # For compliance: Placeholder for input (facilitates future dataflow even if unused)
    user_input = agent.receive_parameter('user_input')
    
    endpoint = "https://gomezmig03.github.io/MotivationalAPI/en.json"
    
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # The API returns JSON; ensure serialization for agent output
        phrases = response.json()
        # Only send serializable outputs
        agent.send_output(
            agent_output_name='motivational_phrases',
            agent_result=phrases
        )
    except Exception as e:
        # Handle any HTTP or JSON errors and return as string for debugging within dataflow
        agent.send_output(
            agent_output_name='motivational_phrases',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='MotivationalPhraseRetriever')
    run(agent=agent)

if __name__ == '__main__':
    main()
