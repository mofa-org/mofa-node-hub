from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
#   - requests (install via pip install requests)
#
# Dataflow ports:
#   Input: 'action' (str: one of 'current_temperature', 'all_data_city', 'all_data_all_cities', 'list_cities')
#          'city'   (optional, str: used for 'current_temperature' and 'all_data_city', default 'bern')
#   Output: 'weather_data' (dict or str serialized)

API_BASE_URL = "https://aareguru.existenz.ch/v2018"
DEFAULT_CITY = "bern"
TIMEOUT = 10

def fetch_current_temperature(city):
    url = f"{API_BASE_URL}/today?city={city}"
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def fetch_all_data_city(city):
    url = f"{API_BASE_URL}/current?city={city}"
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def fetch_all_data_all_cities():
    url = f"{API_BASE_URL}/widget"
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def fetch_list_cities():
    url = f"{API_BASE_URL}/cities"
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()

@run_agent
def run(agent: MofaAgent):
    try:
        params = agent.receive_parameters(['action', 'city'])
        action = params.get('action', '').strip().lower()  # always a string
        city = params.get('city', DEFAULT_CITY).strip().lower() or DEFAULT_CITY
        result = None

        if action == 'current_temperature':
            result = fetch_current_temperature(city)
        elif action == 'all_data_city':
            result = fetch_all_data_city(city)
        elif action == 'all_data_all_cities':
            result = fetch_all_data_all_cities()
        elif action == 'list_cities':
            result = fetch_list_cities()
        else:
            result = {'error': f"Invalid action: '{action}'. Supported actions: current_temperature, all_data_city, all_data_all_cities, list_cities."}

        agent.send_output('weather_data', result)
    except Exception as e:
        agent.send_output('weather_data', {'error': str(e)})

def main():
    agent = MofaAgent(agent_name='AareGuruWeatherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
