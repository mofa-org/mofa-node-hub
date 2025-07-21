# Dependencies:
#   - requests
#
# Ensure the requests library is available in your environment.
#   pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

API_ENDPOINT = "https://api.apgy.in/qr/"
TIMEOUT = 10  # seconds
RETRY_ATTEMPTS = 2

@run_agent
def run(agent: MofaAgent):
    # Receive runtime parameters (all as string; validate/convert as needed)
    try:
        params = agent.receive_parameters(['data', 'size'])  # Both required
        data = params.get('data', '')
        size = params.get('size', '')
        if not data or not size:
            raise ValueError("Both 'data' and 'size' parameters are required.")
        try:
            size_int = int(size)
        except Exception:
            raise ValueError("Parameter 'size' must be an integer (pixels)")
    except Exception as e:
        agent.send_output('qr_code_result', {'error': f"Parameter error: {str(e)}"})
        return
    # Prepare GET request
    query_params = {'data': data, 'size': str(size_int)}
    attempt = 0
    response_content = None
    error_message = None
    while attempt < RETRY_ATTEMPTS:
        try:
            resp = requests.get(API_ENDPOINT, params=query_params, timeout=TIMEOUT)
            if resp.status_code == 200:
                # API returns an image/png
                # We'll return the image as a base64 string for serialization
                import base64
                base64_img = base64.b64encode(resp.content).decode('utf-8')
                agent.send_output(
                    agent_output_name='qr_code_result',
                    agent_result={
                        'qr_code_base64': base64_img,
                        'content_type': resp.headers.get('Content-Type', '')
                    }
                )
                return
            else:
                error_message = f"API error: status {resp.status_code}, {resp.text}"
        except Exception as e:
            error_message = str(e)
        attempt += 1
    # Error after retries
    agent.send_output(
        agent_output_name='qr_code_result',
        agent_result={'error': f"QR code generation failed: {error_message}"}
    )

def main():
    agent = MofaAgent(agent_name='QRCodeGeneratorNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
