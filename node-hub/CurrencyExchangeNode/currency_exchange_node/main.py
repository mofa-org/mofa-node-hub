from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input handling: user_input is required so other nodes can call, but actual API method selection by 'action' param
        user_input = agent.receive_parameter('user_input')  # To maintain node-linking consistency
        action = agent.receive_parameter('action')  # Expected values: 'convert', 'rates', 'currencies'
        
        # API key from .env.secret
        api_key = os.getenv('UNIRATE_API_KEY')
        if not api_key:
            raise ValueError("API key not found: please configure UNIRATE_API_KEY in your .env.secret file.")

        base_url = 'https://api.unirateapi.com/api/'
        response = None
 
        if action == 'convert':
            amount = agent.receive_parameter('amount')
            from_currency = agent.receive_parameter('from')
            to_currency = agent.receive_parameter('to')
            # Validate and serialize inputs
            try:
                float(amount)
            except Exception:
                raise ValueError("Amount must be a number.")
            params = {
                'api_key': api_key,
                'amount': amount,
                'from': from_currency,
                'to': to_currency
            }
            url = base_url + 'convert'
        elif action == 'rates':
            from_currency = agent.receive_parameter('from')
            params = {'api_key': api_key, 'from': from_currency}
            url = base_url + 'rates'
        elif action == 'currencies':
            params = {'api_key': api_key}
            url = base_url + 'currencies'
        else:
            raise ValueError(f"Unsupported action: {action}")
        
        # Make API call
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        # Output delivery: all outputs sent to 'currency_exchange_output'
        agent.send_output(
            agent_output_name='currency_exchange_output',
            agent_result=data
        )
    except Exception as e:
        # Error handled within node
        agent.send_output(
            agent_output_name='currency_exchange_output',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CurrencyExchangeNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
