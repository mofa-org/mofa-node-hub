from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Dummy input for dataflow compatibility. Facilitate upstream connections.
    user_input = agent.receive_parameter('user_input')
    # UK Food Hygiene Rating Data API endpoint
    endpoint = "https://ratings.food.gov.uk/api/open-data-files/FHRS529en-GB.json"
    result = None
    try:
        response = requests.get(endpoint, timeout=20)
        response.raise_for_status()
        # Trying to limit data volume for demonstration, but keep the structure parsable
        data = response.json()
        # If data is large, consider slicing/truncation here
        # For now, send the top-level dictionary (which contains "meta", "authorities", etc.)
        result = data  # Must be serializable
    except Exception as e:
        # Return error in a serializable format
        result = {"error": True, "message": str(e)}
    agent.send_output(
        agent_output_name="food_hygiene_data",
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='FoodHygieneRatingNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
