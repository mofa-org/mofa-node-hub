# Dependencies (add to requirements.txt):
# requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameter from the dataflow (as string)
        url = agent.receive_parameter('url')
        if not isinstance(url, str) or not url.strip():
            agent.send_output(
                agent_output_name='markdown_result',
                agent_result={
                    'error': 'Input URL must be a non-empty string.'
                }
            )
            return

        # Endpoint configuration (could also use env, or config file if permitted)
        endpoint = 'https://urltomarkdown.herokuapp.com'
        timeout = 20  # In seconds (can be made configurable)
        api_path = '/'  # API path is root in this case
        service_url = f"{endpoint}?url={requests.utils.quote(url)}"
        
        try:
            resp = requests.get(service_url, timeout=timeout)
            resp.raise_for_status()
            markdown_content = resp.text
            agent.send_output(
                agent_output_name='markdown_result',
                agent_result={'markdown': markdown_content}
            )
        except requests.exceptions.RequestException as req_err:
            agent.send_output(
                agent_output_name='markdown_result',
                agent_result={
                    'error': f'Request to markdown endpoint failed: {str(req_err)}'
                }
            )
    except Exception as ex:
        # Contain ALL exceptions
        agent.send_output(
            agent_output_name='markdown_result',
            agent_result={
                'error': f'Internal error: {str(ex)}'
            }
        )

def main():
    # Agent instantiation with descriptive name
    agent = MofaAgent(agent_name='WebpageMarkdownConverterNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
