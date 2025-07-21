from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Even if no input required, add input port for orchestration compliance
    user_input = agent.receive_parameter('user_input')

    try:
        # Fetch details for discordpartner.com
        resp_one = requests.get('https://api.fishfish.gg/v1/domains/discordpartner.com')
        resp_one.raise_for_status()
        domain_detail = resp_one.json()
    except Exception as e:
        domain_detail = {'error': True, 'message': 'Failed to get discordpartner.com details', 'exception': str(e)}
    
    try:
        # Fetch the list of domains
        resp_all = requests.get('https://api.fishfish.gg/v1/domains')
        resp_all.raise_for_status()
        domains_list = resp_all.json()
    except Exception as e:
        domains_list = {'error': True, 'message': 'Failed to list domains', 'exception': str(e)}

    # Send output: maintain port consistency with node definitions
    agent.send_output(
        agent_output_name='single_domain_details',
        agent_result=domain_detail
    )
    agent.send_output(
        agent_output_name='domains_list',
        agent_result=domains_list
    )

def main():
    agent = MofaAgent(agent_name='DomainDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
