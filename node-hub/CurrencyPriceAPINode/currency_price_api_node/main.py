from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call this agent
    user_input = agent.receive_parameter('user_input')

    api_url = "https://dolarapi.com/v1/dolares"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The API should return JSON, we ensure it's serialized
        result = response.json()
        agent.send_output(
            agent_output_name='currency_prices',
            agent_result=result
        )
    except Exception as e:
        # Output error state in a serializable format
        agent.send_output(
            agent_output_name='currency_prices',
            agent_result={"error": True, "message": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CurrencyPriceAPINode')
    run(agent=agent)

if __name__ == '__main__':
    main()
