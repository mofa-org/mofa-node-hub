# Dependencies: requests
# Ensure 'requests' package is included in requirements.txt for installation.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate calls from other nodes - dummy input to trigger execution.
    user_input = agent.receive_parameter('user_input')
    
    try:
        url = "https://kanjiapi.dev/v1/kanji/%E8%9B%8D"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        kanji_info = response.json()  # Should be dict, already serializable
        agent.send_output(
            agent_output_name='kanji_info',
            agent_result=kanji_info
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='kanji_info',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='KanjiInfoRetriever')
    run(agent=agent)

if __name__ == '__main__':
    main()
