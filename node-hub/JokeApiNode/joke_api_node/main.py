# Dependencies: requests
# Please ensure requests is included in your environment.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Define API endpoints
ENDPOINTS = {
    "blacklist": {
        "url": "https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist",
        "description": "Get Jokes with Blacklist"
    },
    "german": {
        "url": "https://v2.jokeapi.dev/joke/Any?lang=de",
        "description": "Get Jokes (Language German)"
    }
}

@run_agent
def run(agent: MofaAgent):
    try:
        # Input interface: user must provide 'joke_type' as string ('blacklist' or 'german')
        joke_type = agent.receive_parameter('joke_type')
        if joke_type not in ENDPOINTS:
            raise ValueError(f"Invalid joke_type: {joke_type}. Choose 'blacklist' or 'german'.")

        url = ENDPOINTS[joke_type]['url']
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        joke_data = response.json()
        agent.send_output(
            agent_output_name='joke_response',
            agent_result=joke_data  # Dict is serializable
        )
    except Exception as e:
        # Handle errors gracefully, output error info
        agent.send_output(
            agent_output_name='joke_response',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='JokeApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
