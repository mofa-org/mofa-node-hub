from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate compatibility for calling agent: accept dummy input
    # even though no user input is required for HTTP GET
    user_input = agent.receive_parameter('user_input')
    
    try:
        # First endpoint: Generates corporate jargon
        corp_jargon_url = 'https://insult.mattbas.org/api/en_corporate/insult.json'
        corp_response = requests.get(corp_jargon_url, timeout=10)
        corp_response.raise_for_status()
        corp_data = corp_response.json()
        
        # Second endpoint: Generates an insult
        insult_url = 'https://insult.mattbas.org/api/insult.json'
        insult_response = requests.get(insult_url, timeout=10)
        insult_response.raise_for_status()
        insult_data = insult_response.json()

        # Prepare output (ensure serialization)
        output = {
            'corporate_jargon': corp_data.get('insult', ''),
            'insult': insult_data.get('insult', '')
        }
    except Exception as e:
        # Error containment and serialization
        output = {'error': str(e)}
    
    agent.send_output(
        agent_output_name='insult_api_output',
        agent_result=output
    )

def main():
    agent = MofaAgent(agent_name='InsultAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()
