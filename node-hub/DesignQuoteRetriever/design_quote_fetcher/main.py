from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive a user_input to facilitate node chaining, though it's not needed for API
        user_input = agent.receive_parameter('user_input')
        
        api_url = "https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand"
        response = requests.get(api_url, timeout=10)
        if response.status_code != 200:
            agent.send_output(
                agent_output_name="quote_output",
                agent_result={"error": f"API request failed with status code {response.status_code}"}
            )
            return
        quotes = response.json()
        if not isinstance(quotes, list) or not quotes:
            agent.send_output(
                agent_output_name="quote_output",
                agent_result={"error": "No quotes returned from API."}
            )
            return
        # Simplify output: extract content and author
        first_quote = quotes[0]
        quote_text = str(first_quote.get('content', {}).get('rendered', '')).strip()
        quote_author = str(first_quote.get('title', {}).get('rendered', '')).strip()
        result = {
            "quote": quote_text,
            "author": quote_author
        }
        agent.send_output(
            agent_output_name="quote_output",
            agent_result=result
        )
    except Exception as e:
        agent.send_output(
            agent_output_name="quote_output",
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name="DesignQuoteRetriever")
    run(agent=agent)

if __name__ == "__main__":
    main()
