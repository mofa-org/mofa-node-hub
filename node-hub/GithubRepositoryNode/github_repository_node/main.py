from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
#   - requests
# Ensure 'requests' is specified in your environment/dependency list.

IRONOC_API_BASE_URL = "https://ironoc.net/api/"
DOCUMENTATION_URL = "https://ironoc.net/swagger-ui/index.html?ref=freepublicapis.com"
TIMEOUT = 30

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive parameters (all as string; empty string for fallback)
        params = agent.receive_parameters(["action", "username", "repository"])
        action = params.get("action", "").strip().lower()
        username = params.get("username", "").strip() or "conorheffron"
        repository = params.get("repository", "").strip() or "ironoc"

        result = None
        if action == "repo_detail":
            # GET /get-repo-detail?username={username}
            url = f"{IRONOC_API_BASE_URL}get-repo-detail"
            response = requests.get(url, params={"username": username}, timeout=TIMEOUT)
            response.raise_for_status()
            try:
                result = response.json()
            except Exception:
                result = response.text
            output_port = "repo_detail"
        elif action == "repo_issues":
            # GET /get-repo-issue/<username>/<repository>/
            url = f"{IRONOC_API_BASE_URL}get-repo-issue/{username}/{repository}/"
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            try:
                result = response.json()
            except Exception:
                result = response.text
            output_port = "repo_issues"
        else:
            result = {
                "error": "Invalid action. Use 'repo_detail' or 'repo_issues'.",
                "documentation_url": DOCUMENTATION_URL,
            }
            output_port = "error"

    except Exception as e:
        result = {
            "error": str(e),
            "documentation_url": DOCUMENTATION_URL
        }
        output_port = "error"

    agent.send_output(
        agent_output_name=output_port,
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='GithubRepositoryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
