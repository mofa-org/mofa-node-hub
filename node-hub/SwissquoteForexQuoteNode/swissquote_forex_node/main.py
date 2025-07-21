from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests
# Ensure in requirements.txt:
# requests>=2.25.1

SWISSQUOTE_ENDPOINTS = [
    {
        "url": "https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD",
        "description": "Swissquote Forex Trading XAU (Gold) / USD"
    },
    {
        "url": "https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/EUR/USD",
        "description": "Swissquote Forex Trading EUR / USD"
    }
]

def fetch_forex_quotes():
    results = []
    for endpoint in SWISSQUOTE_ENDPOINTS:
        try:
            response = requests.get(endpoint["url"], timeout=10)
            response.raise_for_status()
            data = response.json()
            results.append({
                "description": endpoint["description"],
                "data": data
            })
        except Exception as e:
            results.append({
                "description": endpoint["description"],
                "error": str(e)
            })
    return results

@run_agent
def run(agent: MofaAgent):
    # Add this to facilitate calls from other nodes
    user_input = agent.receive_parameter('user_input')

    try:
        quotes = fetch_forex_quotes()
        # Ensure output is serializable
        agent.send_output(
            agent_output_name='forex_quotes',
            agent_result=quotes
        )
    except Exception as err:
        # Contain any errors and report through the dataflow port
        agent.send_output(
            agent_output_name='forex_quotes',
            agent_result={"error": str(err)}
        )

def main():
    agent = MofaAgent(agent_name='SwissquoteForexQuoteNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
