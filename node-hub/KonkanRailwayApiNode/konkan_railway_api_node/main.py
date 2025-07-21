from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # Facilitates daisy-chain in mofa/dora-rs
    try:
        # Define endpoints
        stations_url = "https://konkan-railway-api.vercel.app/api/v4/fetchStations"
        trains_url = "https://konkan-railway-api.vercel.app/api/v4/fetchTrains"

        # Fetch stations
        stations_response = requests.get(stations_url, timeout=10)
        stations_response.raise_for_status()
        stations_data = stations_response.json()

        # Fetch trains
        trains_response = requests.get(trains_url, timeout=10)
        trains_response.raise_for_status()
        trains_data = trains_response.json()

        output = {
            'stations': stations_data,
            'live_trains': trains_data
        }
        agent.send_output(
            agent_output_name='konkan_railway_data',
            agent_result=output
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='konkan_railway_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='KonkanRailwayApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
