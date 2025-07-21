# Requirements: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # Facilitate external node calls
    # Available actions: 
    #  - get_station_by_id (station_id: int)
    #  - list_stations ()
    #  - list_partner_stations ()
    try:
        import json
        # Parse user input, expecting string-encoded JSON like '{"action": "get_station_by_id", "station_id": 280}'
        try:
            params = json.loads(user_input) if user_input else {}
        except Exception:
            agent.send_output('publibike_output', {'error': 'Input must be a valid JSON string.'})
            return
        action = params.get('action')
        if action == 'get_station_by_id':
            station_id = params.get('station_id', 280)
            try:
                station_id = int(station_id)
            except Exception:
                agent.send_output('publibike_output', {'error': 'station_id must be an integer.'})
                return
            url = f'https://api.publibike.ch/v1/public/stations/{station_id}'
        elif action == 'list_stations':
            url = 'https://api.publibike.ch/v1/public/stations'
        elif action == 'list_partner_stations':
            url = 'https://api.publibike.ch/v1/public/partner/stations'
        else:
            agent.send_output('publibike_output', {'error': 'Invalid or missing action.'})
            return
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            resp_json = resp.json()
            # Ensure output is serializable
            agent.send_output('publibike_output', resp_json)
        except requests.RequestException as e:
            agent.send_output('publibike_output', {'error': str(e)})
        except Exception as e:
            agent.send_output('publibike_output', {'error': f'Failed to parse response: {str(e)}'})
    except Exception as e:
        agent.send_output('publibike_output', {'error': f'Unhandled error: {str(e)}'})

def main():
    agent = MofaAgent(agent_name='PublibikeStationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()