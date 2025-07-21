from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

# Dependency requirements:
# - requests

@run_agent
def run(agent: MofaAgent):
    # Input handling: expects 'html_content' as string on 'html_content' port
    try:
        input_params = agent.receive_parameters(['html_content'])
        html_content = input_params['html_content']
    except Exception as e:
        agent.send_output(
            agent_output_name='pdf_file',
            agent_result=json.dumps({'error': f'Failed to receive input parameter: {str(e)}'})
        )
        return

    # Prepare API details
    endpoint = "https://html2pdf.fly.dev/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {"html": html_content}  # The API expects 'html' key with HTML source code

    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=30)
        if response.status_code != 200:
            agent.send_output(
                agent_output_name='pdf_file',
                agent_result=json.dumps({'error': f'API returned status code: {response.status_code}', 'detail': response.text})
            )
            return

        # The API returns the binary PDF content.
        # To remain serializable, encode the PDF as base64 string.
        import base64
        pdf_base64 = base64.b64encode(response.content).decode('utf-8')
        output_result = {'pdf_base64': pdf_base64}
        agent.send_output(
            agent_output_name='pdf_file',
            agent_result=output_result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='pdf_file',
            agent_result=json.dumps({'error': f'API request failed: {str(e)}'})
        )

def main():
    agent = MofaAgent(agent_name='HtmlToPdfConverterNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
