# Dependencies: requests
# To install: pip install requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

def check_email(email: str, timeout: int = 10) -> dict:
    """
    Calls the UserCheck API to determine if the given email is a temporary address.
    Returns the API JSON response as a dict or a well-formed error dict.
    """
    endpoint = os.getenv("USERCHECK_API_ENDPOINT", "https://api.usercheck.com/email/")
    url = endpoint.rstrip("/") + "/" + email
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        # Ensure response can be serialized
        result = resp.json()
        if not isinstance(result, dict):
            return {"error": True, "message": "API response is not JSON object"}
        return result
    except requests.RequestException as e:
        return {"error": True, "message": str(e)}
    except Exception as e:
        return {"error": True, "message": f"Unexpected error: {str(e)}"}

@run_agent
def run(agent: MofaAgent):
    # For dataflow, even if input not needed, add user_input so other nodes can call this node gracefully
    user_input = agent.receive_parameter('user_input')  # not used, but required by framework
    
    # Accept 'email' parameter if provided (overrides default)
    try:
        params = agent.receive_parameters(['email', 'timeout'])
    except Exception:
        params = {}

    email = params.get('email', None)
    timeout_val = params.get('timeout', None)
    if email is None or email.strip() == '':
        # fallback to default
        email = os.getenv("EMAILCHECKER_DEFAULT_EMAIL", "hello@freepublicapis.com")

    # Convert timeout
    try:
        timeout = int(timeout_val) if timeout_val is not None else 10
    except ValueError:
        timeout = 10
    result = check_email(email, timeout)
    agent.send_output(
        agent_output_name='email_check_result',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='EmailCheckerNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
