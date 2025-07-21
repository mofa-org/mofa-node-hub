from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it, although not strictly required
    user_input = agent.receive_parameter('user_input')
    
    # Prepare output dictionary
    output = {'single_quote': None, 'five_quotes': None, 'error': None}
    try:
        # Fetch single random quote
        single_response = requests.get('https://api.breakingbadquotes.xyz/v1/quotes', timeout=10)
        single_response.raise_for_status()
        output['single_quote'] = single_response.json()  # Should be a list with one dict
    except Exception as e:
        output['error'] = f"Error fetching single quote: {str(e)}"

    try:
        # Fetch five random quotes
        five_response = requests.get('https://api.breakingbadquotes.xyz/v1/quotes/5', timeout=10)
        five_response.raise_for_status()
        output['five_quotes'] = five_response.json()  # Should be a list of dicts
    except Exception as e:
        err = output.get('error', '')
        output['error'] = (err + ' | ' if err else '') + f"Error fetching five quotes: {str(e)}"
    
    # Ensure all outputs are serializable
    agent.send_output(
        agent_output_name='breaking_bad_quotes',
        agent_result=output
    )

def main():
    agent = MofaAgent(agent_name='BreakingBadQuoteNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
#
# This agent has no required input parameter for operation, but receives 'user_input' to maintain node-call compatibility as required by the mofa/dora agent pattern.
# Outputs (dataflow ports):
#   - breaking_bad_quotes: { 'single_quote': list, 'five_quotes': list, 'error': str or None }
#
# All errors are contained in the 'error' field in the output.