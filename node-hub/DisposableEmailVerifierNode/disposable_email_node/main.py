from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
#   requests
# Ensure 'requests' is installed and declare in your requirements.

def check_domain_disposable(domain: str) -> dict:
    """Checks if a domain is a disposable email service."""
    try:
        api_url = f"https://throwaway.cloud/api/v1/domain/{domain}"
        resp = requests.get(api_url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e), "success": False}

def check_email_disposable(email: str) -> dict:
    """Checks if an email is a disposable email service."""
    try:
        api_url = f"https://throwaway.cloud/api/v1/email/{email}"
        resp = requests.get(api_url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e), "success": False}

@run_agent
def run(agent: MofaAgent):
    # Input ports: 'domain' or 'email' (accepts strings; only one required per call)
    # Check both, but prioritize domain if both present
    params = agent.receive_parameters(['domain', 'email'])

    response = None
    if params.get('domain'):
        domain = params['domain'].strip()
        response = check_domain_disposable(domain)
        dataflow_port = 'domain_check_result'
    elif params.get('email'):
        email = params['email'].strip()
        response = check_email_disposable(email)
        dataflow_port = 'email_check_result'
    else:
        # Facilitate other nodes for input discovery
        user_input = agent.receive_parameter('user_input')
        agent.send_output(
            agent_output_name='error',
            agent_result={"error": "Either 'domain' or 'email' parameter must be provided.", "success": False}
        )
        return

    # Ensure serializable output
    agent.send_output(
        agent_output_name=dataflow_port,
        agent_result=response
    )

def main():
    agent = MofaAgent(agent_name='DisposableEmailVerifierNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
