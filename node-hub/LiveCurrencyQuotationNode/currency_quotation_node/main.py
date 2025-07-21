from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate integration with other nodes, even though there is no real input, we receive a dummy input
    user_input = agent.receive_parameter('user_input')
    
    api_url = 'https://fastapiproject-1-eziw.onrender.com/blue'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        # API returns JSON - ensure it is serializable (dict)
        result = response.json()
    except requests.RequestException as e:
        # Contain errors within the agent boundary
        result = {'error': True, 'message': str(e)}
    except Exception as ex:
        result = {'error': True, 'message': f'Unexpected error: {str(ex)}'}

    agent.send_output(
        agent_output_name='currency_quotation',
        agent_result=result  # dict is serializable
    )

def main():
    agent = MofaAgent(agent_name='LiveCurrencyQuotationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
