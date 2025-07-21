# Dependencies:
#   - requests  # install with: pip install requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input chaining
    user_input = agent.receive_parameter('user_input')

    epigram_endpoint = 'https://perl.is/random'
    try:
        response = requests.get(epigram_endpoint, timeout=10)
        response.raise_for_status()
        data = response.text.strip()  # API returns plaintext
        # Ensure output is serializable - send as string wrapped in dict
        output_payload = {'epigram': data}
        agent.send_output(
            agent_output_name='epigram_output',
            agent_result=output_payload
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='epigram_output',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='PerlisEpigramNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
