from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    TelegaMailingNode
    - Create new mailing (limit 1000 recipients)
    - Get mailing status by mailing id
    Input requirements (as JSON string):
    {
        "action": "create" or "status",
        "mailing_data": {...},  # required for "create"
        "mailing_id": "..."    # required for "status"
    }
    Output: dict with API response
    """
    try:
        user_input = agent.receive_parameter('user_input')  # Required for dataflow compatibility
        input_json = agent.receive_parameter('input_json')
        try:
            params = json.loads(input_json)
        except Exception as e:
            agent.send_output(
                agent_output_name='telega_response',
                agent_result={"error": f"Invalid JSON: {str(e)}"}
            )
            return
        # Load env variables
        api_key = os.getenv('TELEGASEND_API_KEY')
        if not api_key:
            agent.send_output(
                agent_output_name='telega_response',
                agent_result={"error": "Missing TELEGASEND_API_KEY in environment."}
            )
            return
        # Load config
        api_base_url = os.getenv('TELEGASEND_API_BASE_URL', 'https://app.telegasend.ru/api/v1')
        timeout = int(os.getenv('REQUEST_TIMEOUT', '30'))

        action = params.get('action', '').strip().lower()
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

        if action == 'create':
            mailing_data = params.get('mailing_data')
            if not mailing_data or not isinstance(mailing_data, dict):
                agent.send_output('telega_response', {"error": "Missing or invalid 'mailing_data' for create action."})
                return
            url = f"{api_base_url}/mailing"
            try:
                resp = requests.post(url, json=mailing_data, headers=headers, timeout=timeout)
                resp.raise_for_status()
                result = resp.json()
            except Exception as e:
                agent.send_output('telega_response', {"error": f"POST /mailing failed: {str(e)}"})
                return
            agent.send_output('telega_response', result)
            return

        elif action == 'status':
            mailing_id = params.get('mailing_id')
            if not mailing_id:
                agent.send_output('telega_response', {"error": "Missing 'mailing_id' for status action."})
                return
            url = f"{api_base_url}/mailing/{mailing_id}"
            try:
                resp = requests.get(url, headers=headers, timeout=timeout)
                resp.raise_for_status()
                result = resp.json()
            except Exception as e:
                agent.send_output('telega_response', {"error": f"GET /mailing/:id failed: {str(e)}"})
                return
            agent.send_output('telega_response', result)
            return
        else:
            agent.send_output('telega_response', {"error": "Invalid action. Expected 'create' or 'status'."})
    except Exception as ex:
        agent.send_output('telega_response', {"error": f"Agent error: {str(ex)}"})

def main():
    agent = MofaAgent(agent_name='TelegaMailingNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
# Dependencies:
# requests
# python-dotenv (for .env loading if used in deployment)
#
# Environment Variables (set in .env):
# TELEGASEND_API_KEY (required)
# TELEGASEND_API_BASE_URL (optional, default https://app.telegasend.ru/api/v1)
# REQUEST_TIMEOUT (optional, default 30)
#
# Send all data as JSON string via 'input_json'.
# 'user_input' port is required due to dora-rs node compatibility.
# Output always via 'telega_response' dataflow port.
"""