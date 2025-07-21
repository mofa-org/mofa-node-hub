from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Input Handling: Accept params from dataflow
        params = agent.receive_parameters(['lat', 'lng', 'tzid'])
        lat = params.get('lat')
        lng = params.get('lng')
        tzid = params.get('tzid')
        
        # Prepare API endpoint based on presence of tzid
        if tzid:
            endpoint = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&tzid={tzid}'
        else:
            endpoint = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}'
        
        # Make REST API request
        response = requests.get(endpoint)
        response.raise_for_status()
        result_json = response.json()
        
        # Output Serialization
        agent.send_output(
            agent_output_name='sunrise_sunset_info',
            agent_result=result_json  # dict is serializable
        )
    except Exception as e:
        # Error handling: Output error as string
        agent.send_output(
            agent_output_name='sunrise_sunset_info',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='SunriseSunsetNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   requests
#
# Dataflow ports:
#   Input: 'lat' (str), 'lng' (str), optional 'tzid' (str)
#   Output: 'sunrise_sunset_info' (dict or error dict)
#
# Usage:
#   Provide latitude and longitude as strings (and optionally tzid) to retrieve sunrise/sunset data.