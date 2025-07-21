# WebsiteScreenshotExtractor: A dora-rs MofaAgent agent for fetching website screenshots and metadata via screenshotof.com API
# Documentation: https://screenshotof.com?ref=freepublicapis.com
# Dependencies: requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input from dataflow port. To facilitate node linkage, always accept 'user_input'.
        user_input = agent.receive_parameter('user_input')  # Required for IO consistency.
        # Receive target_url to screenshot (string)
        target_url = agent.receive_parameter('target_url')
        # Receive mode: 'current' or 'historical'
        mode = agent.receive_parameter('mode')  # string: 'current' or 'historical'
        # For historical mode, optionally accept date (format: YYYY-MM)
        date = agent.receive_parameter('date') if mode == 'historical' else None

        # Validate target_url
        if not isinstance(target_url, str) or not target_url.strip():
            raise ValueError("Invalid or empty target_url provided.")
        target_url = target_url.strip()

        # Build endpoint
        base = 'https://screenshotof.com/'
        if mode == 'current':
            endpoint = f'{base}{target_url}?f=json'
        elif mode == 'historical':
            if not date or not isinstance(date, str):
                raise ValueError("Date parameter required for historical mode, format: YYYY-MM")
            endpoint = f'{base}{target_url}/{date}?f=json'
        else:
            raise ValueError("Unknown mode. Use 'current' or 'historical'.")

        # Perform GET request
        resp = requests.get(endpoint, timeout=20)
        resp.raise_for_status()
        data = resp.json()  # Should be serializable (dict)

        # Output response via agent port 'screenshot_data'.
        agent.send_output('screenshot_data', data)
    except Exception as e:
        # Error containment: return error info as output
        agent.send_output('screenshot_data', {'error': str(e)})

def main():
    agent = MofaAgent(agent_name='WebsiteScreenshotExtractor')
    run(agent=agent)

if __name__ == '__main__':
    main()
