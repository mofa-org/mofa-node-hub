# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Input interface:
        action: 'by_id', 'list', or 'daily'
        param: For action == 'by_id', this is the endpoint suffix, e.g. '700_de'
    Output on dataflow ports:
        'bird_data': JSON/dict response depending on the chosen action
    """
    try:
        # To facilitate other nodes, even if not always needed
        user_input = agent.receive_parameter('user_input')

        # Obtain parameters
        params = agent.receive_parameters(['action', 'param'])
        action = params.get('action', '').strip().lower()
        param = params.get('param', '').strip()

        base_url = 'https://www.vogelwarte.ch/wp-content/assets/json/bird/'
        result = None

        if action == 'by_id':
            if not param:
                raise ValueError("Missing 'param' for action 'by_id'. Example: '700_de'")
            url = f"{base_url}{param}.json"
        elif action == 'list':
            url = f"{base_url}list_de.json"
        elif action == 'daily':
            url = f"{base_url}bird_of_the_day.json"
        else:
            raise ValueError("Invalid 'action'. Use 'by_id', 'list' or 'daily'.")

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        try:
            result = response.json()
        except Exception:
            result = response.text  # In case not JSON, return as string

        agent.send_output(
            agent_output_name='bird_data',
            agent_result=result
        )

    except Exception as e:
        # Structured error response
        agent.send_output(
            agent_output_name='bird_data',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='BirdSpeciesNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
