# Dependencies:
# - requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent fetches data from 3D or 2D Cartoons public APIs according to 'cartoon_type' input: '3d' or '2d'.
    Input: cartoon_type ('3d' or '2d', as string)
    Output: (serialized list of cartoons or error message) via port 'cartoon_data'
    """
    try:
        cartoon_type = agent.receive_parameter('cartoon_type')
        cartoon_type = cartoon_type.strip().lower() if isinstance(cartoon_type, str) else ''
        if cartoon_type == '3d':
            url = 'https://api.sampleapis.com/cartoons/cartoons3D'
        elif cartoon_type == '2d':
            url = 'https://api.sampleapis.com/cartoons/cartoons2D'
        else:
            agent.send_output(
                agent_output_name='cartoon_data',
                agent_result={'error': 'Invalid cartoon_type. Use "3d" or "2d".'}
            )
            return

        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        cartoon_data = resp.json()
        agent.send_output(
            agent_output_name='cartoon_data',
            agent_result=cartoon_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='cartoon_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CartoonApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
