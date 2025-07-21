from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate dataflow even if no parameter required.
        user_input = agent.receive_parameter('user_input')
        
        # Get domain as single string parameter (extendable)
        domain = agent.receive_parameter('domain')
        if not isinstance(domain, str) or not domain.strip():
            raise ValueError("'domain' parameter must be a non-empty string.")

        # Retrieve API token from environment
        api_token = os.getenv('COMPANY_ENRICH_TOKEN')
        if not api_token:
            raise EnvironmentError("API token not set in environment variable 'COMPANY_ENRICH_TOKEN'.")
        
        api_url = f"https://api.companyenrich.com/companies/enrich?domain={domain}&token={api_token}"

        response = requests.get(api_url, timeout=15)
        if response.status_code != 200:
            raise RuntimeError(f"API request failed (status {response.status_code}): {response.text}")
        
        # Try to parse JSON, fallback to text
        try:
            result = response.json()
        except Exception:
            result = response.text
        
        # Dataflow output
        agent.send_output(
            agent_output_name='company_enrich_response',
            agent_result=result
        )
    except Exception as err:
        agent.send_output(
            agent_output_name='company_enrich_response',
            agent_result={'error': str(err)}
        )

def main():
    agent = MofaAgent(agent_name='CompanyEnrichmentNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests (install via `pip install requests`)
- Environment variable COMPANY_ENRICH_TOKEN must be set via .env.secret

Inputs:
- 'domain' (string): target company domain (e.g., 'google.com')
- 'user_input': placeholder to facilitate upstream compatibility (string, content ignored)

Outputs:
- 'company_enrich_response': dict or string (API response or error message)
"""