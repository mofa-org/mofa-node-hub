from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

ADVICE_BASE_URL = "https://api.adviceslip.com/"
TIMEOUT = 10

@run_agent
def run(agent: MofaAgent):
    # To facilitate chaining, always receive a default input
    user_input = agent.receive_parameter('user_input')
    try:
        # Receive keyword input
        keyword = agent.receive_parameter('keyword')
        if keyword and len(str(keyword).strip()) > 0:
            # Search advice by keyword
            api_url = f"{ADVICE_BASE_URL}advice/search/{keyword}"
            response = requests.get(api_url, timeout=TIMEOUT)
            response.raise_for_status()
            try:
                data = response.json()
            except Exception as e:
                agent.send_output(
                    agent_output_name='api_error',
                    agent_result={"error": "Response JSON decode failed", "details": str(e)}
                )
                return
            # Ensure output is serializable
            agent.send_output(
                agent_output_name='advice_data',
                agent_result=data
            )
        else:
            # Get random advice
            api_url = f"{ADVICE_BASE_URL}advice"
            response = requests.get(api_url, timeout=TIMEOUT)
            response.raise_for_status()
            try:
                data = response.json()
            except Exception as e:
                agent.send_output(
                    agent_output_name='api_error',
                    agent_result={"error": "Response JSON decode failed", "details": str(e)}
                )
                return
            agent.send_output(
                agent_output_name='advice_data',
                agent_result=data
            )
    except requests.exceptions.RequestException as e:
        agent.send_output(
            agent_output_name='api_error',
            agent_result={"error": "API request failed", "details": str(e)}
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='agent_error',
            agent_result={"error": "Unhandled exception", "details": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='AdviceApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Dataflow Ports:
- Input:
    - 'keyword' (str, optional): Keyword to search advices; if empty, gets random advice
    - 'user_input': Default passthrough to ensure compatibility in chained nodes
- Output:
    - 'advice_data': API result (dict)
    - 'api_error': API or decoding errors (dict)
    - 'agent_error': Other uncaught errors (dict)

Stateless, self-contained and fully dora-rs compliant.
"""