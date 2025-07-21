from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # As required by node design, accept a generic input to facilitate calls from other nodes.
        user_input = agent.receive_parameter('user_input')
        # Optionally, log or ignore 'user_input' since this API requires no payload.
        
        endpoint = "https://realip.cc"  # As per config
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        # Ensure response is JSON-serializable
        try:
            result = response.json()
        except Exception:
            # Fallback to text if not valid JSON
            result = response.text
        agent.send_output(
            agent_output_name='ip_info',
            agent_result=result if isinstance(result, (dict, list, str)) else str(result)
        )
    except Exception as e:
        # Contain all errors
        agent.send_output(
            agent_output_name='ip_info',
            agent_result={
                'error': True,
                'message': f'Failed to fetch IP info: {str(e)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='RealIpNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests>=2.25

Output port:
- 'ip_info': returns IP info dict/string, or error message dict.

Input expectations (for node compatibility):
- Receives parameter 'user_input' (contents ignored but required for node chaining compliance.)
"""