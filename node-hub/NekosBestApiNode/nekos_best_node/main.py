from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# dependencies: requests

@run_agent
def run(agent: MofaAgent):
    """
    NekosBestApiNode dora-rs agent: Access nekos.best endpoints for hug images, tickle gifs, or a dynamic endpoint list.
    Inputs:
      - endpoint_type: 'hug', 'tickle', or 'endpoints'.
    Outputs:
      - nekosbest_output: API response (dict)
    """
    try:
        params = agent.receive_parameters(['endpoint_type'])
        endpoint_type = params.get('endpoint_type', '').strip().lower()
        
        # Map input type to endpoint
        endpoint_map = {
            'hug': 'https://nekos.best/api/v2/hug?amount=10',
            'tickle': 'https://nekos.best/api/v2/tickle?amount=10',
            'endpoints': 'https://nekos.best/api/v2/endpoints'
        }

        if endpoint_type not in endpoint_map:
            agent.send_output(
                agent_output_name='nekosbest_output',
                agent_result={
                    'error': True,
                    'message': f"Invalid endpoint_type '{endpoint_type}'. Choose from 'hug', 'tickle', or 'endpoints'."
                }
            )
            return

        url = endpoint_map[endpoint_type]
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            out_data = resp.json()
            agent.send_output(
                agent_output_name='nekosbest_output',
                agent_result=out_data  # dict - guaranteed serializable
            )
        except Exception as e:
            agent.send_output(
                agent_output_name='nekosbest_output',
                agent_result={
                    'error': True,
                    'message': f'API error: {str(e)}'
                }
            )
    except Exception as main_e:
        agent.send_output(
            agent_output_name='nekosbest_output',
            agent_result={
                'error': True,
                'message': f'Agent error: {str(main_e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='NekosBestApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
