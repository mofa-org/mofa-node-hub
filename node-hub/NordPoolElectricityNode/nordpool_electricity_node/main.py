# Dependencies: requests (install via pip)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent to fetch Nord Pool Spot electricity prices from Elering dashboard API.
    Two dataflow input ports are supported:
    1. 'mode' (str): Either 'current' or 'range'. Determines if agent fetches current price or price range.
    2. For 'range' mode: 'start' (str, ISO8601), 'end' (str, ISO8601). For 'current' mode: no additional input needed.
    Outputs:
    - 'electricity_price': dict (API response as dictionary)
    If input is missing or error occurs, sends error message to the same dataflow port.
    """
    try:
        # Required by dora-rs: facilitate other nodes to call
        user_input = agent.receive_parameter('user_input')
        mode = agent.receive_parameter('mode')  # 'current' or 'range', str
        mode = mode.strip().lower() if mode else ''
        
        if mode == 'current':
            # Fetch current electricity price for Estonia
            url = "https://dashboard.elering.ee/api/nps/price/EE/current"
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            data = response.json()
            agent.send_output('electricity_price', data)
        elif mode == 'range':
            params = agent.receive_parameters(['start', 'end'])
            start = params.get('start', '').strip()
            end = params.get('end', '').strip()
            
            if not start or not end:
                # Validate required inputs
                agent.send_output(
                    agent_output_name='electricity_price',
                    agent_result={'error': 'Missing required parameters: start and/or end'}
                )
                return
            # Fetch prices in range
            url = "https://dashboard.elering.ee/api/nps/price"
            req_params = {'start': start, 'end': end}
            response = requests.get(url, params=req_params, timeout=20)
            response.raise_for_status()
            data = response.json()
            agent.send_output('electricity_price', data)
        else:
            agent.send_output(
                agent_output_name='electricity_price',
                agent_result={'error': "Parameter 'mode' must be 'current' or 'range'"}
            )
    except Exception as e:
        err_msg = {'error': f'Exception: {str(e)}'}
        agent.send_output('electricity_price', err_msg)

def main():
    agent = MofaAgent(agent_name='NordPoolElectricityNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
