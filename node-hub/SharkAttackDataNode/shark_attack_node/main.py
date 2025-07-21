from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

"""
Dependencies:
- requests: for HTTP requests. Add to requirements.txt: requests>=2.0.0
"""

@run_agent
def run(agent: MofaAgent):
    """
    Fetches shark attack data for August 2023 (default, can adjust via user_input) from OpenDataSoft API.
    Input:
        user_input (optional): Query string for refined search (e.g. '2023/08', format: 'YYYY/MM').
    Output:
        agent_output_name='shark_attack_results': List/dict of API result or error message.
    """
    try:
        # Facilitate other nodes to call this agent
        user_input = agent.receive_parameter('user_input')
        base_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records"
        params = {
            'limit': '20',
            'refine': f'date:"{user_input}"' if user_input else 'date:"2023/08"'
        }
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()  # dict, guaranteed serializable
        agent.send_output(
            agent_output_name='shark_attack_results',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='shark_attack_results',
            agent_result={"error": True, "message": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='SharkAttackDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
