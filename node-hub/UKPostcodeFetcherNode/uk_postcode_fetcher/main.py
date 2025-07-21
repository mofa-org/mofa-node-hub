from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    This agent fetches UK postcode information using postcodes.io.
    Use input 'action' as 'random' (fetch a random postcode),
    or 'specific' (fetch information for a given postcode string parameter 'postcode').
    Outputs are sent to 'postcode_result'.
    """
    try:
        params = agent.receive_parameters(['action', 'postcode'])  # postcode may be unused
        action = params.get('action', '').strip().lower()
        postcode = params.get('postcode', '').strip()
        timeout = 10  # can be updated if required

        if action == 'random':
            url = 'https://api.postcodes.io/random/postcodes'
        elif action == 'specific':
            if not postcode:
                agent.send_output(
                    agent_output_name='postcode_result',
                    agent_result={
                        'error': 'Missing required parameter: postcode.'
                    }
                )
                return
            url = f'https://api.postcodes.io/postcodes/{postcode.replace(" ", "%20")}'
        else:
            agent.send_output(
                agent_output_name='postcode_result',
                agent_result={
                    'error': "Invalid action. Must be 'random' or 'specific'."
                }
            )
            return

        response = requests.get(url, timeout=timeout)
        try:
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='postcode_result',
                agent_result={'error': f'HTTP or JSON decode error: {str(e)}'}
            )
            return

        agent.send_output(
            agent_output_name='postcode_result',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='postcode_result',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='UKPostcodeFetcherNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# ---
# Dependencies:
# - requests