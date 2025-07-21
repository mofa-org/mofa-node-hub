from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate upstream calls even though there are no required inputs
    user_input = agent.receive_parameter('user_input')  # Not used, for compatibility
    
    api_url = "https://api.adviceslip.com/advice/search/try1"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The API is expected to return JSON
        try:
            data = response.json()  # This could be dict or list
        except Exception as e:
            agent.send_output(
                agent_output_name='advice_search_result',
                agent_result={
                    'error': 'Failed to decode JSON',
                    'exception': str(e),
                    'text': response.text
                }
            )
            return
        agent.send_output(
            agent_output_name='advice_search_result',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='advice_search_result',
            agent_result={
                'error': 'API request failed',
                'exception': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='AdviceSlipSearchNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
