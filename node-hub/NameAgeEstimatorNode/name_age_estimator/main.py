from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling: expects 'name' parameter (as string)
        name_input = agent.receive_parameter('name')
        if not name_input or not isinstance(name_input, str):
            raise ValueError('Input parameter "name" must be a non-empty string.')

        # API Integration: call Agify.io
        api_url = f"https://api.agify.io?name={name_input}"
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        api_data = response.json()
        # Ensure serialization and output structure
        output_data = {
            'name': api_data.get('name'),
            'age': api_data.get('age'),
            'count': api_data.get('count')
        }
        agent.send_output(
            agent_output_name='estimated_age',
            agent_result=output_data
        )
    except Exception as e:
        # Structured error output
        agent.send_output(
            agent_output_name='estimated_age',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='NameAgeEstimatorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests

Ensure 'requests' is available in your environment.
'''
