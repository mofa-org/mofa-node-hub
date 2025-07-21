from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependencies: requests (add to requirements.txt)
# No direct filesystem or env access. All config via framework or code.

@run_agent
def run(agent: MofaAgent):
    try:
        # Input: receive an address query string
        query = agent.receive_parameter('q')
        if not isinstance(query, str):
            raise ValueError('Input parameter "q" must be a string.')

        # API configuration
        ENDPOINT = "https://www.als.gov.hk/lookup"
        TIMEOUT = 10
        MAX_RETRY = 3
        QUERY_PARAM = "q"

        session = requests.Session()
        retries = 0
        response_data = None

        while retries < MAX_RETRY:
            try:
                params = {QUERY_PARAM: query}
                resp = session.get(ENDPOINT, params=params, timeout=TIMEOUT)
                resp.raise_for_status()
                response_data = resp.json()
                break
            except Exception as e:
                retries += 1
                if retries >= MAX_RETRY:
                    raise e

        # Output: send API result to dataflow port, ensure serialization
        agent.send_output(
            agent_output_name='address_lookup_result',
            agent_result=response_data  # Already JSON serializable
        )
    except Exception as err:
        # Complete error containment
        agent.send_output(
            agent_output_name='address_lookup_result',
            agent_result={'error': str(err)}
        )

def main():
    agent = MofaAgent(agent_name='AddressLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
