from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies: requests
# This agent retrieves country information based on country name or capital.

@run_agent
def run(agent: MofaAgent):
    try:
        # Input: expects 'name' or 'capital' (at least one must be provided)
        params = agent.receive_parameters(['name', 'capital'])
        country_name = params.get('name', '').strip()
        capital_name = params.get('capital', '').strip()

        if country_name:
            url = f'https://restcountries.com/v3.1/name/{country_name}'
        elif capital_name:
            url = f'https://restcountries.com/v3.1/capital/{capital_name}'
        else:
            agent.send_output(
                agent_output_name='country_info_error',
                agent_result={'error': 'Either "name" or "capital" input must be provided.'}
            )
            return
        
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            agent.send_output(
                agent_output_name='country_info_error',
                agent_result={'error': f'API returned status {response.status_code}', 'detail': response.text}
            )
            return
        
        try:
            country_info = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='country_info_error',
                agent_result={'error': 'Error parsing country info JSON', 'detail': str(e)}
            )
            return
        
        # Output the full country info response (list/dict)
        agent.send_output(
            agent_output_name='country_info_response',
            agent_result=country_info
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='country_info_error',
            agent_result={'error': 'Unexpected error in CountryInfoRetriever', 'detail': str(ex)}
        )

def main():
    agent = MofaAgent(agent_name='CountryInfoRetriever')
    run(agent=agent)

if __name__ == '__main__':
    main()
