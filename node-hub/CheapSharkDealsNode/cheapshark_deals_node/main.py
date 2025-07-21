from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input parameter for game title
        title = agent.receive_parameter('title')  # Always string per requirements
        if title is None or title.strip() == '':
            # If not provided, default to 'batman' as per config
            title = 'batman'
        else:
            title = str(title)
        # Compose API endpoint (GET)
        base_url = "https://www.cheapshark.com/api/1.0/games"
        params = {'title': title}
        response = requests.get(base_url, params=params, timeout=10)
        if response.status_code != 200:
            result = {'error': True, 'message': f"CheapShark API returned status code {response.status_code}"}
        else:
            # Try to parse response JSON
            try:
                deals_data = response.json()
                # Ensure serializability
                result = {'error': False, 'deals': deals_data}
            except Exception as parse_exc:
                result = {'error': True, 'message': f"Failed to parse API response: {parse_exc}"}
    except Exception as exc:
        result = {'error': True, 'message': str(exc)}
    # Deliver result
    agent.send_output(
        agent_output_name='deals_output',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='CheapSharkDealsNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests
# Ensure to install with: pip install requests
