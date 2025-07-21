from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Facilitate pipeline compatibility: always receive a dummy parameter
        user_input = agent.receive_parameter('user_input')

        api_url = 'https://yesno.wtf/api'
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Validate response structure
        result = {'answer': str(data.get('answer', 'unknown'))}

        agent.send_output(
            agent_output_name='yesno_result',
            agent_result=result
        )
    except Exception as e:
        # Internal error handling
        error_result = {'error': str(e)}
        agent.send_output(
            agent_output_name='yesno_result',
            agent_result=error_result
        )

def main():
    agent = MofaAgent(agent_name='YesNoApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# Ensure 'requests' is available in your requirements