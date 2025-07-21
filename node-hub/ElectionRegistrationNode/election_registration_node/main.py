# Dependencies: requests (install via pip if missing)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

API_BASE = "https://dedline-api.netlify.app"

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate other nodes to call it even if not used
        user_input = agent.receive_parameter('user_input')

        # Define supported endpoints
        endpoints = {
            "last_minute_accepted": f"{API_BASE}/lastMinuteAccepted.json",
            "all_states": f"{API_BASE}/states.json",
            "online_not_accepted": f"{API_BASE}/onlineNotAccepted.json",
            "state_info": f"{API_BASE}/states/{{state_abbr}}.json"
        }

        # Get 'action' parameter to determine API target (expected: [last_minute_accepted, all_states, online_not_accepted, state_info])
        params = agent.receive_parameters(['action', 'state_abbr'])
        action = params.get('action', '').strip()
        state_abbr = params.get('state_abbr', '').strip().upper()
        result = None
        error_msg = None

        if action == 'last_minute_accepted':
            url = endpoints['last_minute_accepted']
        elif action == 'all_states':
            url = endpoints['all_states']
        elif action == 'online_not_accepted':
            url = endpoints['online_not_accepted']
        elif action == 'state_info':
            if not state_abbr:
                error_msg = "Missing required parameter: state_abbr for state_info action."
            url = endpoints['state_info'].format(state_abbr=state_abbr)
        else:
            error_msg = f"Invalid or unsupported action requested: '{action}'."
            url = None

        if error_msg:
            agent.send_output(
                agent_output_name='error',
                agent_result={"error": error_msg}
            )
            return

        resp = requests.get(url, timeout=8)
        try:
            resp.raise_for_status()
        except Exception as ex:
            agent.send_output(
                agent_output_name='error',
                agent_result={"error": f"HTTP error: {str(ex)}", "status_code": resp.status_code}
            )
            return
        try:
            data = resp.json()
        except Exception:
            # Try fallback to text
            data = resp.text
        agent.send_output(
            agent_output_name='api_result',
            agent_result=data
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='error',
            agent_result={"error": str(ex)}
        )

def main():
    agent = MofaAgent(agent_name='ElectionRegistrationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
