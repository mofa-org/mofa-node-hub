from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    This agent fetches recent data from two endpoints regarding:
        - SARS-CoV-2 in wastewater
        - Influenza A in wastewater
    Both endpoints return data about gene copies per 100,000 people and positive individuals.

    Inputs: string "pathogen_type" (either 'sars-cov-2' or 'influenza-a'), or empty for both
    Outputs: dict with keys 'sars-cov-2' and/or 'influenza-a', mapped to endpoint response JSON
    """
    try:
        # Receive user input to guide which pathogen's data to fetch
        pathogen_type = agent.receive_parameter('pathogen_type')  # Accept "sars-cov-2", "influenza-a" or "all" (empty also = all)
        if pathogen_type is None:
            pathogen_type = ''
        pathogen_type = str(pathogen_type).strip().lower()
        
        # Endpoint config
        endpoints = {
            "sars-cov-2": "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100187/records?limit=20",
            "influenza-a": "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100302/records?limit=20"
        }
        results = {}

        # Decide which endpoints to query
        selected = []
        if not pathogen_type or pathogen_type == 'all':
            selected = list(endpoints.keys())
        elif pathogen_type in endpoints:
            selected = [pathogen_type]
        else:
            agent.send_output(
                agent_output_name='wastewater_pathogen_results',
                agent_result={"error": f"Invalid pathogen_type '{pathogen_type}'. Use 'sars-cov-2', 'influenza-a', or leave empty for both."}
            )
            return
        
        # Query APIs
        for kind in selected:
            try:
                resp = requests.get(endpoints[kind], timeout=10)
                resp.raise_for_status()
                data = resp.json()
                results[kind] = data
            except Exception as e:
                results[kind] = {"error": f"Failed to fetch {kind}: {str(e)}"}

        agent.send_output(
            agent_output_name='wastewater_pathogen_results',
            agent_result=results
        )

    except Exception as exc:
        agent.send_output(
            agent_output_name='wastewater_pathogen_results',
            agent_result={"error": f"Internal error: {str(exc)}"}
        )

def main():
    agent = MofaAgent(agent_name='WastewaterPathogenMonitor')
    run(agent=agent)

if __name__ == '__main__':
    main()

'''
Dependencies:
- requests
'''
