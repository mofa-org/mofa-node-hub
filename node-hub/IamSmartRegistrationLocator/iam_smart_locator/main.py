# Dependencies: requests (add to requirements.txt)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes even if no input is required
    user_input = agent.receive_parameter('user_input')
    
    endpoints = [
        "https://www.digitalpolicy.gov.hk/open_data/iam_smart/iAM-Smart-RegistrationMobileTeamService.json",
        "https://www.digitalpolicy.gov.hk/open_data/iam_smart/iAM-Smart-RegistrationServiceCounter.json",
        "https://www.digitalpolicy.gov.hk/open_data/iam_smart/iAM-Smart-SelfRegistrationKiosk.json",
    ]
    results = {}
    try:
        for url in endpoints:
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                results[url] = resp.json()
            except requests.exceptions.RequestException as e:
                results[url] = {'error': str(e)}
    except Exception as e:
        # fatal error in agent, encapsulate all in results
        results['fatal_error'] = str(e)
    # Serialize result and send through dataflow port
    agent.send_output(
        agent_output_name='registration_data',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='IamSmartRegistrationLocator')
    run(agent=agent)

if __name__ == '__main__':
    main()
