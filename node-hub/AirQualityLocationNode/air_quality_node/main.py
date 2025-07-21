from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # This agent does not require input, but to facilitate compatibility add a placeholder input receive:
    user_input = agent.receive_parameter('user_input')

    outputs = {}

    try:
        resp_letzigrund = requests.get('https://api.openaq.org/v2/locations/1236033', timeout=10)
        resp_letzigrund.raise_for_status()
        outputs['letzigrund_info'] = resp_letzigrund.json()
    except Exception as e:
        outputs['letzigrund_info'] = {'error': str(e)}

    try:
        resp_locations = requests.get('https://api.openaq.org/v2/locations', timeout=10)
        resp_locations.raise_for_status()
        outputs['all_locations'] = resp_locations.json()
    except Exception as e:
        outputs['all_locations'] = {'error': str(e)}

    # As per requirement, serialization is mandatory
    agent.send_output(
        agent_output_name='air_quality_outputs',
        agent_result=outputs
    )

def main():
    agent = MofaAgent(agent_name='AirQualityLocationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests

Dataflow output ports:
- air_quality_outputs: dict with keys 'letzigrund_info' and 'all_locations', or error messages.
'''
