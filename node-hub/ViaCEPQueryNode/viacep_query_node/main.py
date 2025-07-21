from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # For orchestration compatibility, even if no input is needed
        user_input = agent.receive_parameter('user_input')

        # ViaCEP API endpoint (fixed example with CEP: 01001000)
        url = "https://viacep.com.br/ws/01001000/json/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result = response.json()
        # Ensure serialization (dict is serializable)
        agent.send_output(
            agent_output_name='viacep_response',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='viacep_response',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ViaCEPQueryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
