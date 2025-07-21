# Dependencies: requests (document in requirements.txt)
# requirements.txt:
# requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # No input expected, but allow for future pipeline compatibility
        user_input = agent.receive_parameter('user_input')
        
        endpoint = "https://datos.gob.es/apidata/catalog/dataset?_sort=title&_pageSize=10&_page=0"
        response = requests.get(endpoint, timeout=15)
        response.raise_for_status()

        # Parse JSON safely
        try:
            data = response.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='api_error',
                agent_result={'error': 'Invalid JSON received from API', 'details': str(e)}
            )
            return

        agent.send_output(
            agent_output_name='fuel_dataset',
            agent_result=data  # Dict is natively serializable
        )
    except requests.exceptions.RequestException as e:
        agent.send_output(
            agent_output_name='api_error',
            agent_result={'error': 'HTTP request failed', 'details': str(e)}
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='node_error',
            agent_result={'error': 'Unexpected node error', 'details': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='SpanishFuelDatasetNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
