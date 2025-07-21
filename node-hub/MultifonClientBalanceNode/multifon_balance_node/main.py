# multifon_balance_node.py
# Dependencies: requests; python-dotenv (for loading environment variables)
# Ensure you include requests and python-dotenv in your requirements.txt

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
from dotenv import load_dotenv

@run_agent
def run(agent: MofaAgent):
    try:
        # Load environment variables from .env.secret (handled by platform; here for clarity)
        load_dotenv('.env.secret')
        
        # Required to facilitate upstream node calls per instructions
        user_input = agent.receive_parameter('user_input')

        # Get credentials from environment
        login = os.environ.get('MULTIFON_LOGIN')
        password = os.environ.get('MULTIFON_PASSWORD')

        if not login or not password:
            agent.send_output(
                agent_output_name='balance_result',
                agent_result={
                    'error': True,
                    'message': 'API credentials missing in environment variables.'
                }
            )
            return

        endpoint = 'https://sm.megafon.ru/sm/client/balance'
        try:
            response = requests.get(
                endpoint,
                params={'login': login, 'password': password},
                timeout=30
            )
        except requests.RequestException as e:
            agent.send_output(
                agent_output_name='balance_result',
                agent_result={
                    'error': True,
                    'message': f'API connection error: {str(e)}'
                }
            )
            return

        try:
            data = response.json()
        except Exception:
            data = response.text

        result = {
            'status_code': response.status_code,
            'data': data,
            'error': False
        }
        if response.status_code != 200:
            result['error'] = True
            result['message'] = 'Non-200 status code from Multifon API.'

        # Guarantee serializable output
        agent.send_output(
            agent_output_name='balance_result',
            agent_result=result
        )
    except Exception as ex:
        agent.send_output(
            agent_output_name='balance_result',
            agent_result={
                'error': True,
                'message': f'Unhandled agent error: {str(ex)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='MultifonClientBalanceNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
