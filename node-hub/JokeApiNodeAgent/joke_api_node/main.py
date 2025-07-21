from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # Facilitate other nodes to call it

    # Input: category (can be 'fat', 'old', or 'random'). Accepts string; fallback to 'random' if not recognized
    try:
        category = agent.receive_parameter('category').strip().lower()
    except Exception:
        category = 'random'
    
    try:
        timeout = 10  # default timeout in seconds
        base_url = "https://www.yomama-jokes.com/api/v1/jokes/"
        if category == 'fat':
            endpoint = base_url + 'fat/'
        elif category == 'old':
            endpoint = base_url + 'old/random/'
        else:
            endpoint = base_url + 'random/'
        
        response = requests.get(endpoint, timeout=timeout)
        response.raise_for_status()
        # The API sometimes returns JSON with {'joke': ...} or {'jokes': [...]} etc.
        data = response.json()
        if isinstance(data, dict) and 'joke' in data:
            result = data['joke']
        elif isinstance(data, dict) and 'jokes' in data and isinstance(data['jokes'], list):
            result = data['jokes']
        else:
            result = data
        # Validate serialization
        if not isinstance(result, (str, list, dict)):
            result = str(result)

        agent.send_output(
            agent_output_name='joke_data',
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='joke_data',
            agent_result=f"Error getting joke: {str(e)}"
        )

def main():
    agent = MofaAgent(agent_name='JokeApiNodeAgent')
    run(agent=agent)

if __name__ == '__main__':
    main()
