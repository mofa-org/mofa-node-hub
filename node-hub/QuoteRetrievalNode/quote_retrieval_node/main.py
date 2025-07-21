from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate other nodes to call it (even though not strictly needed here)
    user_input = agent.receive_parameter('user_input')
    try:
        api_url = "https://www.quoterism.com/api/quotes/random"
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The API responds with JSON
        quote_data = response.json()
        # Ensure it's serializable and robust
        result = {
            "status": "success",
            "quote": quote_data
        }
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e)
        }
    agent.send_output(
        agent_output_name="quote_output",
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name="QuoteRetrievalNode")
    run(agent=agent)

if __name__ == "__main__":
    main()

'''
Dependencies:
- requests (ensure this package is installed in the agent's environment)
Output Port:
- quote_output: Delivers a dict containing API response or error
Input Handling:
- Receives 'user_input' (dummy parameter for dataflow compliance)
'''
