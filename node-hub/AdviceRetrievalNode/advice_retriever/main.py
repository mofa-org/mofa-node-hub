from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Required dependencies: requests
#   pip install requests

@run_agent
def run(agent: MofaAgent):
    """
    AdviceRetrievalNode Agent for fetching advice from https://kk-advice.koyeb.app/api
    - agent_output_name can be 'all_advice' or 'random_advice' depending on the requested API endpoint.
    - Receives 'mode' parameter: 'all' for all advice, 'random' for random advice.
    """
    try:
        # Input handling (single string parameter indicating mode)
        mode = agent.receive_parameter('mode')  # Expected: 'all' or 'random'
        if mode is None:
            raise ValueError("Missing required input parameter: 'mode'")
        mode = mode.strip().lower()

        # API endpoint configuration
        BASE_URL = "https://kk-advice.koyeb.app/api"
        ENDPOINTS = {
            'all': '/advice/all',
            'random': '/advice'
        }
        TIMEOUT = 10  # seconds
        RETRIES = 2

        if mode not in ENDPOINTS:
            raise ValueError(f"Invalid mode value: {mode}. Expected 'all' or 'random'.")

        url = BASE_URL + ENDPOINTS[mode]

        last_exception = None
        for attempt in range(RETRIES + 1):
            try:
                response = requests.get(url, timeout=TIMEOUT)
                response.raise_for_status()
                data = response.json()  # allow output to be dict/list
                # Output delivery (ensure serializable)
                agent.send_output(
                    agent_output_name=('all_advice' if mode=='all' else 'random_advice'),
                    agent_result=data
                )
                return
            except Exception as e:
                last_exception = e

        # If all retries failed
        raise last_exception

    except Exception as err:
        # Error containment
        error_msg = {
            'error': True,
            'error_msg': str(err)
        }
        # Output error information through both ports for robustness
        agent.send_output('all_advice', error_msg)
        agent.send_output('random_advice', error_msg)

def main():
    agent = MofaAgent(agent_name='AdviceRetrievalNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
