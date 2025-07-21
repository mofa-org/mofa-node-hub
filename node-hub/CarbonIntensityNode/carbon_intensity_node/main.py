from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receive input to facilitate dataflow, even though not required
    user_input = agent.receive_parameter('user_input')
    outputs = {}
    try:
        # 1. Get Carbon Intensity factors for each fuel type
        resp_factors = requests.get("https://api.carbonintensity.org.uk/intensity/factors", timeout=10)
        outputs['factors'] = resp_factors.json() if resp_factors.ok else {'error': resp_factors.text}
    except Exception as e:
        outputs['factors'] = {'error': str(e)}

    try:
        # 2. Get Carbon Intensity data for today
        resp_today = requests.get("https://api.carbonintensity.org.uk/intensity/date", timeout=10)
        outputs['today'] = resp_today.json() if resp_today.ok else {'error': resp_today.text}
    except Exception as e:
        outputs['today'] = {'error': str(e)}

    try:
        # 3. Get Carbon Intensity data for specific date
        resp_specific = requests.get("https://api.carbonintensity.org.uk/intensity/date/2024-05-19", timeout=10)
        outputs['specific_date'] = resp_specific.json() if resp_specific.ok else {'error': resp_specific.text}
    except Exception as e:
        outputs['specific_date'] = {'error': str(e)}

    try:
        # 4. Get Carbon Intensity data for current half hour
        resp_halfhr = requests.get("https://api.carbonintensity.org.uk/intensity", timeout=10)
        outputs['current_halfhour'] = resp_halfhr.json() if resp_halfhr.ok else {'error': resp_halfhr.text}
    except Exception as e:
        outputs['current_halfhour'] = {'error': str(e)}

    # Output all results via dedicated port
    agent.send_output(
        agent_output_name='carbon_intensity_data',
        agent_result=outputs
    )

def main():
    agent = MofaAgent(agent_name='CarbonIntensityNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests (install via: pip install requests)

Dataflow Ports:
- Input: 'user_input' (required for dora-rs stateless chain, even if unused)
- Output: 'carbon_intensity_data' (delivers all queried data as a dict)
'''
