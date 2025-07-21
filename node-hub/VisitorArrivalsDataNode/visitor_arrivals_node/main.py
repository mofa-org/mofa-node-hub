from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # To facilitate compatibility with frameworks that require input, receive a placeholder parameter.
        user_input = agent.receive_parameter('user_input')

        # API configuration (can be adjusted for future updates/yml config handling if needed)
        api_endpoint = "https://www.censtatd.gov.hk/api/get.php?id=650-80001&lang=en&full_series=1"
        timeout = 30  # seconds
        
        response = requests.get(api_endpoint, timeout=timeout)
        response.raise_for_status()  # Raise HTTPError for bad status codes
        try:
            data = response.json()
        except Exception as json_err:
            agent.send_output(
                agent_output_name='error',
                agent_result={
                    'error': 'JSONDecodeError',
                    'message': str(json_err)
                }
            )
            return
        agent.send_output(
            agent_output_name='visitor_arrivals_data',
            agent_result=data
        )
    except requests.Timeout:
        agent.send_output(
            agent_output_name='error',
            agent_result={
                'error': 'Timeout',
                'message': f'Request to API endpoint timed out after {timeout} seconds.'
            }
        )
    except requests.RequestException as req_err:
        agent.send_output(
            agent_output_name='error',
            agent_result={
                'error': 'RequestException',
                'message': str(req_err)
            }
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result={
                'error': 'UnhandledException',
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='VisitorArrivalsDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
