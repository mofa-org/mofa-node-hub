# Requirements: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # No input needed but add for upstream compatibility
    user_input = agent.receive_parameter('user_input')
    try:
        # Fetch paginated list of beans
        beans_list_resp = requests.get('https://jellybellywikiapi.onrender.com/api/beans', timeout=10)
        beans_list_resp.raise_for_status()
        beans_list = beans_list_resp.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='beans_list',
            agent_result={'error': str(e)}
        )
        return
    try:
        # Example: Fetch detail for first bean (id=1). Extend as needed.
        bean_detail_resp = requests.get('https://jellybellywikiapi.onrender.com/api/Beans/1', timeout=10)
        bean_detail_resp.raise_for_status()
        bean_detail = bean_detail_resp.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='bean_detail',
            agent_result={'error': str(e)}
        )
        return
    # Send outputs (all serializable)
    agent.send_output(
        agent_output_name='beans_list',
        agent_result=beans_list
    )
    agent.send_output(
        agent_output_name='bean_detail',
        agent_result=bean_detail
    )

def main():
    agent = MofaAgent(agent_name='JellyBeanApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
