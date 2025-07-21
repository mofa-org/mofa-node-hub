# adresse_api_node.py
# Dependencies: requests
#   Install via: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input for method selection: 'reverse' or 'search'
        method = agent.receive_parameter('method')  # expects 'reverse' or 'search'
        # Receive additional parameters depending on method
        params = {}
        if method == 'reverse':
            # Get longitude & latitude as strings, convert to float
            param_dict = agent.receive_parameters(['lon', 'lat'])
            try:
                lon = float(param_dict.get('lon', '2.37'))
                lat = float(param_dict.get('lat', '48.357'))
            except ValueError:
                agent.send_output(
                    agent_output_name='adresse_api_error',
                    agent_result='{"error": "Invalid lon or lat value"}'
                )
                return
            url = f'https://api-adresse.data.gouv.fr/reverse/'
            payload = {'lon': lon, 'lat': lat}
        elif method == 'search':
            # Get 'q' parameter
            query = agent.receive_parameter('q')
            if not isinstance(query, str) or not query.strip():
                agent.send_output(
                    agent_output_name='adresse_api_error',
                    agent_result='{"error": "Missing or invalid search query (q)"}'
                )
                return
            url = f'https://api-adresse.data.gouv.fr/search/'
            payload = {'q': query}
        else:
            agent.send_output(
                agent_output_name='adresse_api_error',
                agent_result='{"error": "Invalid method (must be reverse or search)"}'
            )
            return

        # Process API call
        try:
            response = requests.get(url, params=payload, timeout=10)
            response.raise_for_status()
            # API returns JSON
            result = response.json()
        except Exception as api_exc:
            agent.send_output(
                agent_output_name='adresse_api_error',
                agent_result=json.dumps({"error": str(api_exc)})
            )
            return

        # Output result via appropriate port
        agent.send_output(
            agent_output_name='adresse_api_response',
            agent_result=result
        )
    except Exception as exc:
        agent.send_output(
            agent_output_name='adresse_api_error',
            agent_result=json.dumps({'error': f'Internal error: {str(exc)}'})
        )

def main():
    agent = MofaAgent(agent_name='AdresseApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
