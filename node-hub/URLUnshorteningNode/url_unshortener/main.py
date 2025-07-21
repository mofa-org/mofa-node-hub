# Dependencies: requests, python-dotenv
# Documentation: https://unshorten.me/api?ref=freepublicapis.com
# .env must set: UNSHORTEN_AUTH_HEADER

import os
import requests
from dotenv import load_dotenv
from mofa.agent_build.base.base_agent import MofaAgent, run_agent

def unshorten_url(short_url: str, auth_header: str) -> dict:
    """
    Calls the Unshorten.me API to unshorten a given short URL.
    Args:
        short_url (str): The URL to unshorten.
        auth_header (str): Authorization header for the API.
    Returns:
        dict: Response dictionary from the API or error information.
    """
    api_url = f"https://unshorten.me/json/{short_url}"
    headers = {
        "Accept": "application/json",
    }
    if auth_header:
        headers["Authorization"] = auth_header
    try:
        response = requests.get(api_url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}

@run_agent
def run(agent: MofaAgent):
    # Receives input shortened_url as string
    shortened_url = agent.receive_parameter('shortened_url')
    load_dotenv()
    auth_header = os.getenv('UNSHORTEN_AUTH_HEADER', '')
    result = unshorten_url(shortened_url, auth_header)
    # Always serializable (dict)
    agent.send_output(
        agent_output_name='unshortened_result',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='URLUnshorteningNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
