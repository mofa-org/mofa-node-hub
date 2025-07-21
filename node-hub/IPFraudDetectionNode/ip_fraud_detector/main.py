from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Always receive user_input to facilitate other node calls, per requirements
        user_input = agent.receive_parameter('user_input')
        ip = agent.receive_parameter('ip')
        # Retrieve 'contact' email from environment variables (set via .env.secret)
        contact_email = os.getenv('GETIPINTEL_CONTACT_EMAIL')
        if not contact_email:
            raise ValueError("Contact email not configured in environment variable 'GETIPINTEL_CONTACT_EMAIL'.")
        # Use default format as per configuration
        format_type = 'json'
        # Prepare API request
        endpoint = 'https://check.getipintel.net/check.php'
        params = {
            'ip': ip,
            'contact': contact_email,
            'format': format_type
        }
        response = requests.get(endpoint, params=params, timeout=10)
        if response.status_code != 200:
            raise RuntimeError(f"API Request failed with status code {response.status_code}: {response.text}")
        # The API returns JSON
        try:
            result_json = response.json()
        except Exception:
            raise ValueError(f"Failed to decode JSON from API response: {response.text}")
        # Output delivery (must be serializable)
        agent.send_output(
            agent_output_name='ip_fraud_score',
            agent_result=result_json
        )
    except Exception as e:
        # Handle all errors internally and output as string
        agent.send_output(
            agent_output_name='ip_fraud_score',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='IPFraudDetectionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
