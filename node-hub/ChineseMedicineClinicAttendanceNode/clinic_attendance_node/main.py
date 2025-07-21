from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    ChineseMedicineClinicAttendanceNode Agent
    Fetches annual attendance data for Chinese Medicine Clinics cum Training and Research Centres.
    Input: 'language' (string): one of ['english','simplified-chinese','traditional-chinese']
    Output: JSON data from the corresponding public API endpoint
    Output port: 'attendance_data'
    """
    try:
        # Input: expecting a string parameter 'language'
        language = agent.receive_parameter('language').strip().lower()
        
        endpoints = {
            'simplified-chinese': 'https://www.ha.org.hk/opendata/cmctr/cmctr-attnd-sc.json',
            'english': 'https://www.ha.org.hk/opendata/cmctr/cmctr-attnd-en.json',
            'traditional-chinese': 'https://www.ha.org.hk/opendata/cmctr/cmctr-attnd-tc.json',
        }
        
        if language not in endpoints:
            agent.send_output(
                agent_output_name='attendance_data',
                agent_result={
                    'error': True,
                    'message': f"Invalid language value: '{language}'. Supported: {list(endpoints.keys())}"
                }
            )
            return
        
        url = endpoints[language]
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            agent.send_output(
                agent_output_name='attendance_data',
                agent_result={
                    'error': True,
                    'message': f"Failed to fetch data from endpoint '{url}': {str(e)}"
                }
            )
            return
        
        agent.send_output(
            agent_output_name='attendance_data',
            agent_result=data if isinstance(data, (dict, list)) else str(data)
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='attendance_data',
            agent_result={
                'error': True,
                'message': f"Unhandled error in agent: {str(e)}"
            }
        )

def main():
    agent = MofaAgent(agent_name='ChineseMedicineClinicAttendanceNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests
- mofa.agent_build.base.base_agent (provided by MOFA/dora-rs)
"""