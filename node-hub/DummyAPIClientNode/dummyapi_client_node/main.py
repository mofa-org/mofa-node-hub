# Dependencies: requests
# To install: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this agent
    user_input = agent.receive_parameter('user_input')
    
    # DummyAPI endpoint (no parameters required)
    endpoint = 'https://dummyapi.online/api/products'
    
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()  # Should be serializable (list/dict)
        
        agent.send_output(
            agent_output_name='dummyapi_products',
            agent_result=data
        )
    except requests.RequestException as e:
        # Send error output in standardized format
        agent.send_output(
            agent_output_name='dummyapi_products',
            agent_result={'error': str(e)}
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='dummyapi_products',
            agent_result={'error': f'Unexpected error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='DummyAPIClientNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
