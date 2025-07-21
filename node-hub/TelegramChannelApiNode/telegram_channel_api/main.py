from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitates calling by downstream nodes even if no input is required
    user_input = agent.receive_parameter('user_input')

    # API endpoint configuration
    API_URL = "https://t.me/n9he1"

    try:
        # For demonstration, since this is a Telegram link, a GET request will most likely return the HTML content
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        # Passing content as string (limit output size as appropriate)
        result = {
            "status_code": response.status_code,
            "content": response.text[:2000]  # Limit to first 2000 chars to ensure serialization
        }
    except Exception as e:
        result = {
            "error": True,
            "message": str(e)
        }

    agent.send_output(
        agent_output_name='telegram_channel_response',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='TelegramChannelApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
