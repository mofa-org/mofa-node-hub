from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    RosaryPrayerNode Agent
    Fetches Rosary prayers (text/audio) from public API endpoints based on input selection.
    agent_output_name: "monday_text", "today_audio"
    """
    try:
        # Receive a string parameter indicating which prayer to fetch
        # Supported inputs: 'monday_text' or 'today_audio'
        prayer_type = agent.receive_parameter('prayer_type')

        if not isinstance(prayer_type, str):
            raise ValueError("prayer_type must be a string.")

        # Map for endpoint selection
        endpoints = {
            'monday_text': {
                'url': 'https://the-rosary-api.vercel.app/v1/monday',
                'output_port': 'monday_text',
            },
            'today_audio': {
                'url': 'https://the-rosary-api.vercel.app/v1/today',
                'output_port': 'today_audio',
            },
        }

        if prayer_type not in endpoints:
            raise ValueError(f"Invalid prayer_type: {prayer_type}. Choose from: {list(endpoints.keys())}")

        url = endpoints[prayer_type]['url']
        output_port = endpoints[prayer_type]['output_port']

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # Try to parse as JSON, fallback to text
        try:
            data = response.json()
        except Exception:
            data = response.text

        # Ensure output is serializable
        agent.send_output(
            agent_output_name=output_port,
            agent_result=data
        )
    except Exception as e:
        # Error containment and output
        error_message = {'error': True, 'message': str(e)}
        agent.send_output(
            agent_output_name='error',
            agent_result=error_message
        )

def main():
    agent = MofaAgent(agent_name='RosaryPrayerNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
# - requests: For HTTP requests. Install with `pip install requests`
# Input port:   prayer_type (string: 'monday_text' or 'today_audio')
# Output ports: 'monday_text', 'today_audio', 'error'
