# Dependencies: requests
# To install: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive the zip code as string input
        zip_code = agent.receive_parameter('zip_code')
        
        if not zip_code:
            raise ValueError("Input parameter 'zip_code' is required.")
        
        # Only digits validation (optional, as API might accept other formats)
        # zip_code = str(zip_code).strip()
        
        endpoint = f"https://ziptasticapi.com/{zip_code}"
        resp = requests.get(endpoint, timeout=8)
        if resp.status_code != 200:
            result = {
                'error': True,
                'error_msg': f"Failed to get location info: HTTP {resp.status_code}"
            }
        else:
            # Ensure JSON serializability
            data = resp.json()
            # Ziptastic may return {'error': 'Invalid Zip Code'}. Handle this..
            if 'error' in data:
                result = {
                    'error': True,
                    'error_msg': data['error']
                }
            else:
                # Always return country, state, city as strings if available
                result = {
                    'error': False,
                    'country': str(data.get('country', '')),
                    'state': str(data.get('state', '')),
                    'city': str(data.get('city', '')),
                    'zip_code': str(zip_code)
                }
            
        agent.send_output(
            agent_output_name='location_info',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='location_info',
            agent_result={
                'error': True,
                'error_msg': str(e)
            }
        )

def main():
    # Example agent_name can be set here - update if needed for deployment
    agent = MofaAgent(agent_name='ZipCodeLocationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
