from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Placeholder input for dataflow compatibility
def main():
    agent = MofaAgent(agent_name='CrossrefMetadataNode')
    
    try:
        user_input = agent.receive_parameter('user_input')  # For dataflow triggers
        crossref_url = "https://api.crossref.org/heartbeat"
        
        response = requests.get(crossref_url, timeout=10)
        response.raise_for_status()
        
        try:
            output_data = response.json()
        except Exception:
            # If the response is not JSON, fallback to raw text
            output_data = response.text
        
        agent.send_output(agent_output_name='crossref_heartbeat', agent_result=output_data)
    except Exception as e:
        agent.send_output(agent_output_name='crossref_heartbeat', agent_result={"error": str(e)})

if __name__ == '__main__':
    main()
