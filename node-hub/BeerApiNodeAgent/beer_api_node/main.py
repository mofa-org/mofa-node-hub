# Dependencies:
# - requests
# Ensure 'requests' is installed in your environment:
# pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

API_BASE_URL = "https://punkapi.online/v3/beers"

@run_agent
def run(agent: MofaAgent):
    try:
        # Determine which operation to perform
        params = agent.receive_parameters(['operation', 'value'])
        operation = params.get('operation', '').strip().lower()  # 'list', 'random', 'by_id'
        value = params.get('value', '').strip()                  # page number (str) or id (str)

        if operation == 'list':
            # Get a page of beers, value is page number (str, optional)
            page_num = 1
            if value:
                try:
                    page_num = int(value)
                    if page_num < 1:
                        raise ValueError
                except Exception:
                    agent.send_output('error', f"Invalid page number: {value}")
                    return
            url = f"{API_BASE_URL}?page={page_num}"

        elif operation == 'random':
            url = f"{API_BASE_URL}/random"

        elif operation == 'by_id':
            # Get by ID, value should be beer id (str, required, 1-415)
            try:
                beer_id = int(value)
                if not (1 <= beer_id <= 415):
                    agent.send_output('error', f"ID out of range (1-415): {value}")
                    return
            except Exception:
                agent.send_output('error', f"Invalid id: {value}")
                return
            url = f"{API_BASE_URL}/{beer_id}"

        else:
            agent.send_output('error', f"Unknown operation: '{operation}'. Supported: 'list', 'random', 'by_id'")
            return

        # Perform the HTTP request
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            agent.send_output('error', str(e))
            return

        # Output serialization
        try:
            output_data = json.dumps(data, ensure_ascii=False)
        except Exception as e:
            agent.send_output('error', f"Serialization error: {str(e)}")
            return
        agent.send_output(agent_output_name='api_response', agent_result=output_data)
    except Exception as e:
        agent.send_output('error', f"Agent error: {str(e)}")

def main():
    agent = MofaAgent(agent_name='BeerApiNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()
