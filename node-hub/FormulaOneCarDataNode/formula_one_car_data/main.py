from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependencies: requests
# Documentation: https://openf1.org/?ref=freepublicapis.com
# This agent fetches Formula 1 drivers and car telemetry data from the OpenF1 API.

OPENF1_BASE_URL = "https://api.openf1.org/v1"
ENDPOINTS = {
    "drivers": "/drivers",
    "car_data": "/car_data"
}

def fetch_openf1_data(endpoint: str, params: dict):
    try:
        full_url = f"{OPENF1_BASE_URL}{endpoint}"
        response = requests.get(full_url, params=params, timeout=10)
        response.raise_for_status()
        # Ensure result is serializable (convert to dict/list)
        try:
            return response.json()
        except Exception as e:
            return {"error": "Failed to parse JSON result: " + str(e)}
    except requests.RequestException as e:
        return {"error": "HTTP error: " + str(e)}
    except Exception as e:
        return {"error": "Unexpected error: " + str(e)}

@run_agent
def run(agent: MofaAgent):
    # Universal input for ease of orchestration
    user_input = agent.receive_parameter('user_input')

    # Receive core parameters; default to YAML config values if not provided
    driver_number = agent.receive_parameter('driver_number') or '1'
    session_key = agent.receive_parameter('session_key') or '9158'
    mode = agent.receive_parameter('mode') or 'drivers'  # 'drivers' or 'car_data'
    speed = agent.receive_parameter('speed')

    try:
        # Case 1: Fetch basic driver info
        if mode == 'drivers':
            params = {
                'driver_number': driver_number,
                'session_key': session_key
            }
            data = fetch_openf1_data(ENDPOINTS['drivers'], params)
            agent.send_output(
                agent_output_name='openf1_drivers',
                agent_result=data
            )
        # Case 2: Fetch car telemetry data (with speed filter)
        elif mode == 'car_data':
            # Use default speed if not given
            speed_value = speed if speed else '315'
            params = {
                'driver_number': driver_number,
                'session_key': session_key,
                'speed>=': speed_value
            }
            data = fetch_openf1_data(ENDPOINTS['car_data'], params)
            agent.send_output(
                agent_output_name='openf1_car_data',
                agent_result=data
            )
        else:
            agent.send_output(
                agent_output_name='error',
                agent_result={"error": "Invalid mode requested. Choose 'drivers' or 'car_data'."}
            )
    except Exception as e:
        # Full error containment
        agent.send_output(
            agent_output_name='error',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='FormulaOneCarDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
