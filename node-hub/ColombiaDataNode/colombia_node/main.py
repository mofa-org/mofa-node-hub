from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate pipeline call even if no input required
    user_input = agent.receive_parameter('user_input')
    
    try:
        # Define endpoints
        president_url = "https://api-colombia.com/api/v1/President"
        tourist_url = "https://api-colombia.com/api/v1/TouristicAttraction"
        
        # Make requests
        pres_resp = requests.get(president_url, timeout=10)
        tour_resp = requests.get(tourist_url, timeout=10)
        
        pres_resp.raise_for_status()
        tour_resp.raise_for_status()
        
        # Parse JSON data
        president_data = pres_resp.json()
        touristic_data = tour_resp.json()
        
        # Package result
        result = {
            "president": president_data,
            "touristic_attractions": touristic_data
        }
        # Send output on consistent port name
        agent.send_output(
            agent_output_name='colombia_data',
            agent_result=result
        )
    except Exception as e:
        # Contain all errors, report as string
        agent.send_output(
            agent_output_name='colombia_data',
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name='ColombiaDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

"""
Dependencies:
- requests

Dataflow Output Port:
- colombia_data: dict with president and touristic_attractions keys, or error report
"""