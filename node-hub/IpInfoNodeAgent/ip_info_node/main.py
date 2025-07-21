from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate other nodes to call this agent, receive an optional user_input parameter
    user_input = agent.receive_parameter('user_input')
    
    api_url = "https://ipinfo.io/json"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # API returns JSON; ensure serialization for the dora-rs agent framework
        result_data = response.json()  # dict, auto serializable
        agent.send_output(
            agent_output_name='ip_info',
            agent_result=result_data
        )
    except Exception as e:
        # Error containment and reporting
        agent.send_output(
            agent_output_name='ip_info',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='IpInfoNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()
