# Dependencies:
# Requires: requests
# In requirements.txt: requests>=2.0.0

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate dataflow even if no input needed (per instructions)
    user_input = agent.receive_parameter('user_input')
    
    try:
        response = requests.get(
            'http://api.open-notify.org/iss-now.json',
            timeout=10
        )
        response.raise_for_status() # Raise HTTPError for bad responses (4xx/5xx)
        data = response.json()
        # Validate serialization: only dict, list, or str
        if not isinstance(data, (dict, list, str)):
            data = str(data)
        agent.send_output(
            agent_output_name='iss_location',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='iss_location',
            agent_result={'error': True, 'msg': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ISSTrackerNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
