from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameter (required by design, even if not used)
        user_input = agent.receive_parameter('user_input')
        url = agent.receive_parameter('url')  # Target web page URL (string)
    except Exception as e:
        agent.send_output(
            agent_output_name='phantomjscloud_error',
            agent_result={'error': f'Input parameter error: {str(e)}'}
        )
        return

    # Load config from environment and yml
    phantomjs_key = os.environ.get('PHANTOMJS_CLOUD_KEY', None)
    if not phantomjs_key:
        agent.send_output(
            agent_output_name='phantomjscloud_error',
            agent_result={'error': 'Missing PHANTOMJS_CLOUD_KEY in environment'}
        )
        return

    base_endpoint = f"https://phantomjscloud.com/api/browser/v2/{phantomjs_key}/"
    request_dict = {
        "url": url,
        "renderType": "plainText",
        "outputAsJson": True
    }
    payload = {"request": json.dumps(request_dict)}

    try:
        resp = requests.get(
            base_endpoint,
            params=payload,
            timeout=30
        )
        resp.raise_for_status()
    except requests.RequestException as req_err:
        agent.send_output(
            agent_output_name='phantomjscloud_error',
            agent_result={'error': f'HTTP error: {str(req_err)}'}
        )
        return

    # Response processing
    try:
        json_result = resp.json()
    except Exception as e:
        agent.send_output(
            agent_output_name='phantomjscloud_error',
            agent_result={'error': f'Invalid JSON response: {str(e)}'}
        )
        return

    # Validate output serializability
    try:
        json.dumps(json_result)
    except Exception as e:
        agent.send_output(
            agent_output_name='phantomjscloud_error',
            agent_result={'error': f'Output not serializable: {str(e)}'}
        )
        return

    agent.send_output(
        agent_output_name='phantomjscloud_response',
        agent_result=json_result
    )

def main():
    agent = MofaAgent(agent_name='PhantomJSCloudNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
