from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input from upstream even though not required here
    user_input = agent.receive_parameter('user_input')  # Dummy input to maintain dataflow compatibility
    try:
        api_url = 'https://api.miip.my'
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The expected format: {"ip": "203.0.113.12", "country": "Malaysia", "countryCode": "MY"}
        api_result = response.json()
        # Ensure serialization (dict is allowed per the spec)
        agent.send_output(
            agent_output_name='ip_country_info',
            agent_result=api_result
        )
    except Exception as e:
        # Output error info in a controlled serializable form
        agent.send_output(
            agent_output_name='ip_country_info',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='IPCountryLookupNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
