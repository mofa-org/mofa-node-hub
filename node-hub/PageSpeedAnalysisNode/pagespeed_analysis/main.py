from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import os
import requests

@run_agent
def run(agent: MofaAgent):
    """
    dora-rs compliant PageSpeed Analysis Agent
    - Receives: 'target_url' (str)
    - Outputs: 'pagespeed_data' (dict)
    """
    try:
        # Input (as REQUIRED by framework, even if config says 'url')
        user_input = agent.receive_parameter('user_input')  # For dora-rs port chaining convenience
        target_url = agent.receive_parameter('target_url')
        if not target_url or not isinstance(target_url, str):
            raise ValueError("Input parameter 'target_url' is required and must be a string.")

        # Get API key from env (.env.secret)
        api_key = os.getenv('PAGESPEED_API_KEY')
        if not api_key:
            raise ValueError("Missing API key. Please set the PAGESPEED_API_KEY in your environment.")

        # Optional config from runtime variables or defaults
        locale = os.getenv('PAGESPEED_LOCALE', 'en_US')
        strategy = os.getenv('PAGESPEED_STRATEGY', 'mobile')
        timeout = int(os.getenv('PAGESPEED_TIMEOUT', '30'))

        endpoint_url = f"https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed"
        params = {
            "url": target_url,
            "key": api_key,
            "locale": locale,
            "strategy": strategy
        }

        response = requests.get(endpoint_url, params=params, timeout=timeout)
        response.raise_for_status()

        # Serialization check: response JSON will be a dict
        result = response.json()
        agent.send_output(
            agent_output_name='pagespeed_data',
            agent_result=result
        )
    except Exception as e:
        # Always return error info but DO NOT crash
        agent.send_output(
            agent_output_name='pagespeed_data',
            agent_result={"error": True, "message": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='PageSpeedAnalysisNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
