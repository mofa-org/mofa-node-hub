from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# External dependency: requests

def fetch_meeting_records(name_of_meeting: str, maximum_records: int, record_packing: str) -> dict:
    endpoint = "https://kokkai.ndl.go.jp/api/meeting_list"
    params = {
        "nameOfMeeting": name_of_meeting,
        "maximumRecords": str(maximum_records),
        "recordPacking": record_packing,
    }
    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {"success": True, "data": data}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)}"}

@run_agent
def run(agent: MofaAgent):
    # Input handling
    # All parameters required for API request; default to preset values if not provided
    params = agent.receive_parameters([
        "name_of_meeting",
        "maximum_records",
        "record_packing"
    ])
    
    # Type conversions and fallbacks
    name_of_meeting = params.get("name_of_meeting") or "東日本大震災"
    try:
        maximum_records = int(params.get("maximum_records", 100))
    except (TypeError, ValueError):
        maximum_records = 100
    record_packing = params.get("record_packing") or "json"

    # Core logic: API Call
    api_result = fetch_meeting_records(
        name_of_meeting=name_of_meeting,
        maximum_records=maximum_records,
        record_packing=record_packing
    )
    
    # Output delivery
    agent.send_output(
        agent_output_name="diet_meeting_records",
        agent_result=api_result  # dict, json-serializable
    )

def main():
    agent = MofaAgent(agent_name="DietMeetingApiNode")
    run(agent=agent)

if __name__ == '__main__':
    main()
