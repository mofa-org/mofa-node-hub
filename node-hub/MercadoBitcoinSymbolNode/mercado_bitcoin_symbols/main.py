# Dependency: requests
# Add to requirements.txt: requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # To facilitate potential upstream connections, expect a placeholder input
    user_input = agent.receive_parameter('user_input')
    api_url = "https://api.mercadobitcoin.net/api/v4/symbols"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        symbols_data = response.json()  # Should be serializable
    except requests.RequestException as e:
        symbols_data = {"error": str(e)}
    except Exception as e:
        symbols_data = {"error": f"Unexpected error: {str(e)}"}

    agent.send_output(
        agent_output_name='symbols',
        agent_result=symbols_data
    )

def main():
    agent = MofaAgent(agent_name='MercadoBitcoinSymbolNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
