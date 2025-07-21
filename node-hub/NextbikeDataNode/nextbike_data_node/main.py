from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    NextbikeDataNode Agent v1
    Retrieves bike-sharing data from the Nextbike public API.
    Parameters (all optional, all as strings):
      - city: fetch for specific city ID, e.g. '1'
      - lat: latitude coordinate for geo search, e.g. '51.34049'
      - lng: longitude coordinate for geo search, e.g. '12.36890'
      - domains: filter by brand/domain, e.g. 'kg'
    Output port:
      - 'api_response': dict (JSON-deserialized API response)
    """
    try:
        # Input gathering (all optional)
        params_dict = agent.receive_parameters(['city', 'lat', 'lng', 'domains'])
        
        # Base config from YAML (defaults)
        base_url = "https://api.nextbike.net/maps/nextbike-live.json"
        timeout = 10  # seconds

        # Prepare query parameters
        params = {}
        if params_dict.get('city'):
            params['city'] = params_dict['city']
        if params_dict.get('lat') and params_dict.get('lng'):
            params['lat'] = params_dict['lat']
            params['lng'] = params_dict['lng']
        if params_dict.get('domains'):
            params['domains'] = params_dict['domains']

        # If no parameters provided, call for entire network
        # If both city and (lat+lng) are present, API prefers lat/lng
        
        resp = requests.get(base_url, params=params if params else None, timeout=timeout)
        try:
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={
                    'error': True,
                    'message': f"API call failed during JSON decode or HTTP error: {str(e)}",
                    'details': resp.text if resp is not None else ''
                }
            )
            return
        # Output serialization: ensure dict
        agent.send_output(
            agent_output_name='api_response',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={
                'error': True,
                'message': f"Agent-level error: {str(e)}"
            }
        )

def main():
    agent = MofaAgent(agent_name='NextbikeDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
