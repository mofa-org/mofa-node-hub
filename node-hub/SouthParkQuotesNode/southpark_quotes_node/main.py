from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    SouthParkQuotesNode Agent:
      - Fetches three random South Park quotes and Kenny-specific quotes via the South Park Quotes API.
      - No required input, so facilitate dataflow input port with a dummy receive for 'user_input'.
      - Both endpoints are GET requests with no parameters.
    """
    # Facilitate dataflow by receiving a dummy input (for orchestration)
    user_input = agent.receive_parameter('user_input')
    api_results = {}
    
    try:
        # Get three random quotes
        resp_3 = requests.get("https://southparkquotes.onrender.com/v1/quotes/3", timeout=8)
        resp_3.raise_for_status()
        api_results['three_quotes'] = resp_3.json()
    except Exception as e:
        api_results['three_quotes'] = {'error': str(e)}
    
    try:
        # Get Kenny quotes
        resp_kenny = requests.get("https://southparkquotes.onrender.com/v1/quotes/search/kenny", timeout=8)
        resp_kenny.raise_for_status()
        api_results['kenny_quotes'] = resp_kenny.json()
    except Exception as e:
        api_results['kenny_quotes'] = {'error': str(e)}

    # Output must be serializable
    agent.send_output(
        agent_output_name='southpark_quotes_api_results',
        agent_result=api_results
    )

def main():
    agent = MofaAgent(agent_name='SouthParkQuotesNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests

Ensure requests is included in your environment. Add to requirements.txt if needed:
requests>=2.25.0
'''
