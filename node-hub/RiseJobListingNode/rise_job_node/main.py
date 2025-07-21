from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling (all params as string; optional: allow overriding defaults via inputs)
        # Allow page, limit, sort, sortedBy, jobLoc as optional params
        params = agent.receive_parameters(['page', 'limit', 'sort', 'sortedBy', 'jobLoc'])

        # Establish defaults from config (yml or use hardcoded fallback)
        endpoint = "https://api.joinrise.io/api/v1/jobs/public"
        default_params = {
            'page': '1',
            'limit': '20',
            'sort': 'desc',
            'sortedBy': 'createdAt',
            'jobLoc': ''
        }
        # Merge user parameters (if blank, fallback to defaults)
        api_params = {}
        for key in default_params:
            val = params.get(key, '')
            api_params[key] = val if val else default_params[key]

        # Type conversion for page & limit
        try:
            api_params['page'] = int(api_params['page'])
        except Exception:
            api_params['page'] = int(default_params['page'])
        try:
            api_params['limit'] = int(api_params['limit'])
        except Exception:
            api_params['limit'] = int(default_params['limit'])

        # Request to API
        response = requests.get(endpoint, params=api_params, timeout=15)
        response.raise_for_status()
        data = response.json()

        # Output through framework
        agent.send_output(
            agent_output_name='job_listings',
            agent_result=data
        )
    except Exception as e:
        error_message = {'error': str(e)}
        agent.send_output(
            agent_output_name='job_listings',
            agent_result=error_message
        )

def main():
    agent = MofaAgent(agent_name='RiseJobListingNode')
    run(agent=agent)

if __name__ == '__main__':
    main()