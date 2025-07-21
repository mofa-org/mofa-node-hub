from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Retrieves today's liturgical calendar entry and the list of available calendars
    using http://calapi.inadiutorium.cz public APIs. No inputs required, but receives 'user_input' to comply with dora-rs stateless interface.
    """
    # Receive input parameter for compliance (stateless chaining, not used)
    user_input = agent.receive_parameter('user_input')
    calendar_today_endpoint = "http://calapi.inadiutorium.cz/api/v0/en/calendars/default/today"
    calendars_list_endpoint = "http://calapi.inadiutorium.cz/api/v0/en/calendars"

    outputs = {
        'today_calendar': None,
        'calendars_list': None,
        'error': None
    }
    try:
        today_resp = requests.get(calendar_today_endpoint, timeout=10)
        today_resp.raise_for_status()
        outputs['today_calendar'] = today_resp.json()
    except Exception as e:
        outputs['error'] = f"Error fetching today's calendar: {str(e)}"
    try:
        list_resp = requests.get(calendars_list_endpoint, timeout=10)
        list_resp.raise_for_status()
        outputs['calendars_list'] = list_resp.json()
    except Exception as e:
        outputs['error'] = (outputs['error'] or "") + f" | Error fetching calendars list: {str(e)}"
    # Output: Both calendar and list (dict)
    agent.send_output(
        agent_output_name='calendar_result',
        agent_result=outputs
    )

def main():
    agent = MofaAgent(agent_name='LiturgicalCalendarNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
