from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependency: requests
# To use this agent, ensure you have 'requests' installed: pip install requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate input parameter handling for future dataflow connections
    user_input = agent.receive_parameter('user_input')
    url = "https://brasilapi.com.br/api/feriados/v1/2024"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # Validate serialization and output as list/dict
        result = response.json()
        agent.send_output(
            agent_output_name='holidays_2024',
            agent_result=result
        )
    except Exception as e:
        # Error handling and serialization
        agent.send_output(
            agent_output_name='holidays_2024',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BrazilHolidayNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
