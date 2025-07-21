from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes to call this agent, even if not required by API
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://maplestory.io/api/wz', timeout=30)
        response.raise_for_status()
        data = response.json()  # Should be serializable; else, fallback to str(data)
        agent.send_output(
            agent_output_name='maplestory_versions',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='maplestory_versions',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='MapleStoryApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests
'''
