# Dependencies:
#   requests: For sending HTTP GET requests
#   (Declare in requirements.txt: requests)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Allow flexible operation for either query, support both "book_language" and "copyright_free" options
        query_type = agent.receive_parameter('query_type')  # 'de' for German books, 'nocopyright' for copyright-free
        
        if query_type == 'de':
            url = "https://gutendex.com/books?languages=de"
        elif query_type == 'nocopyright':
            url = "https://gutendex.com/books?copyright=false"
        else:
            agent.send_output(
                agent_output_name='books_output',
                agent_result={'error': f'Unknown query_type: {query_type}'}
            )
            return
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        try:
            result_json = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='books_output',
                agent_result={'error': f'Failed to parse JSON: {e}'}
            )
            return
        
        agent.send_output(
            agent_output_name='books_output',
            agent_result=result_json  # Already dict, JSON-serializable
        )

    except Exception as e:
        agent.send_output(
            agent_output_name='books_output',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='GutenbergBookNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
