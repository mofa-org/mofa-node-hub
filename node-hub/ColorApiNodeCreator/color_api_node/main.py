from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies: requests
# - Install with: pip install requests

@run_agent
def run(agent: MofaAgent):
    """
    Aggregates color analysis from two endpoints provided by serialif.com.
    No input parameters required for this agent, but 'user_input' parameter is fetched for framework compatibility.
    Outputs a dict with the responses from both endpoints on the 'color_data' port.
    """
    try:
        # For dataflow consistency, allow other nodes to send an (unused) input
        user_input = agent.receive_parameter('user_input')
        
        endpoints = [
            "https://color.serialif.com/aquamarine",
            "https://color.serialif.com/55667788"
        ]
        results = {}
        for url in endpoints:
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status() # HTTP error containment
                # Try JSON first, fallback to text
                try:
                    results[url] = resp.json()
                except Exception:
                    results[url] = resp.text
            except Exception as e:
                # Each endpoint error is handled individually
                results[url] = {'error': str(e)}
        # Validate serialization
        agent.send_output(
            agent_output_name='color_data',
            agent_result=results
        )
    except Exception as err:
        # Framework error containment
        agent.send_output(
            agent_output_name='color_data',
            agent_result={'error': str(err)}
        )

def main():
    agent = MofaAgent(agent_name='ColorApiNodeCreator')
    run(agent=agent)

if __name__ == '__main__':
    main()
