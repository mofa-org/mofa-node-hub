from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate other nodes to call this agent even if no input is strictly required
        user_input = agent.receive_parameter('user_input')  # Accepts string or empty value
        # Optional: parse user_input into URL parameters if provided
        endpoint = "https://dymo.tpeoficial.com/?ch-pg=freepublicapis.com"
        full_url = endpoint
        if user_input and user_input.strip():
            # If user_input is meant to be query params (e.g.: 'key1=val1&key2=val2')
            if '?' in endpoint:
                full_url += '&' + user_input.strip()
            else:
                full_url += '?' + user_input.strip()

        response = requests.get(full_url, timeout=15)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception:
            data = response.text

        # Output result, ensure serialization
        agent.send_output(
            agent_output_name='fraud_detection_result',
            agent_result=data if isinstance(data, (str, dict, list)) else str(data)
        )
    except Exception as e:
        # Contain error and output as string
        agent.send_output(
            agent_output_name='fraud_detection_result',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='MultiAccountFraudDetectionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
