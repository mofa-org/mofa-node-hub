# Dependencies: requests
# To install: pip install requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Get a random Chuck Norris joke, optionally by category. 
    Input port: 'category' (optional, string)
    Output port: 'joke_output' (str or dict)
    """
    try:
        # Try to receive an optional 'category' parameter
        category = agent.receive_parameter('category')
        if category and category.strip():
            endpoint = f"https://api.chucknorris.io/jokes/random?category={category.strip()}"
        else:
            endpoint = "https://api.chucknorris.io/jokes/random"
        
        response = requests.get(endpoint, timeout=5)
        response.raise_for_status()
        data = response.json()
        # Ensure output is serializable
        agent.send_output(
            agent_output_name='joke_output',
            agent_result={"id": data.get("id", ""), "joke": data.get("value", "")}
        )
    except Exception as e:
        # Handle and output error as complaint response
        agent.send_output(
            agent_output_name='joke_output',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ChuckNorrisJokeNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
