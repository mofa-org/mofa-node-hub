from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameters as strings (with default fallbacks)
        params = agent.receive_parameters(['groupSize', 'size', 'bossId', 'page'])
        
        # Type conversion and validation
        group_size = int(params.get('groupSize', '2'))
        size = int(params.get('size', '1'))
        boss_id = int(params.get('bossId', '1'))
        page = int(params.get('page', '0'))

        # Prepare request
        endpoint = "https://secure.runescape.com/m=group_hiscores/v1//groups"
        query_params = {
            'groupSize': group_size,
            'size': size,
            'bossId': boss_id,
            'page': page
        }

        response = requests.get(endpoint, params=query_params, timeout=15)
        response.raise_for_status()
        data = response.json()

        # Ensure output is serializable
        agent.send_output(
            agent_output_name='group_hiscores',
            agent_result=data
        )
    except Exception as e:
        # Error handling: return error as serializable output
        agent.send_output(
            agent_output_name='group_hiscores',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='RunescapeGroupHiscoresNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests