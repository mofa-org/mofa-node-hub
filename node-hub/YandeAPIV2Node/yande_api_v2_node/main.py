# Agent: YandeAPIV2Node
# Description: Queries the YandeRe v2 JSON API endpoint and returns the results.
# Dependencies: requests

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    Queries the YandeRe v2 API endpoint and returns JSON data.
    The agent is stateless and provides error handling for network/API issues.
    No input is required by this agent; a dummy receive_parameter is provided for pipeline compatibility.
    """
    try:
        # Facilitates pipeline calls; not actually used
        user_input = agent.receive_parameter('user_input')
        
        endpoint = "https://yande.re/post.json?api_version=2"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        
        # Ensure response is JSON-serializable
        try:
            data = response.json()
        except Exception as json_err:
            error_result = {
                "error": True,
                "message": f"Failed to decode JSON: {json_err}"
            }
            agent.send_output(
                agent_output_name='yande_api_v2_response',
                agent_result=error_result
            )
            return
        
        # Send output as a list or dict (as returned by the API)
        agent.send_output(
            agent_output_name='yande_api_v2_response',
            agent_result=data
        )
    except Exception as e:
        # Strict error containment
        error_result = {
            "error": True,
            "message": str(e)
        }
        agent.send_output(
            agent_output_name='yande_api_v2_response',
            agent_result=error_result
        )

def main():
    agent = MofaAgent(agent_name='YandeAPIV2Node')
    run(agent=agent)

if __name__ == '__main__':
    main()
