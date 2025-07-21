from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive website URL from the input port
        url_param = agent.receive_parameter('url')
        if not isinstance(url_param, str) or not url_param.strip():
            raise ValueError("The 'url' parameter must be a non-empty string.")

        endpoint = "https://api.websitecarbon.com/site"
        params = {"url": url_param}

        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()  # parse the JSON result
        except requests.RequestException as req_err:
            error_msg = f"Request failed: {str(req_err)}"
            agent.send_output(
                agent_output_name='error',
                agent_result={'error': error_msg}
            )
            return
        except Exception as parse_err:
            error_msg = f"Failed to parse response: {str(parse_err)}"
            agent.send_output(
                agent_output_name='error',
                agent_result={'error': error_msg}
            )
            return

        # Output the website carbon emissions data
        agent.send_output(
            agent_output_name='carbon_results',
            agent_result=data
        )
    except Exception as e:
        # General error handler for the agent
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': str(e)}
        )

def main():
    # Instantiate the Agent
    agent = MofaAgent(agent_name='WebsiteCarbonNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests  # Document this in requirements.txt as requests
