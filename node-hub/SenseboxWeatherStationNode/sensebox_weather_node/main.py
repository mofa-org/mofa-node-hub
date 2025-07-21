from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    Agent to fetch weather data from a public Sensebox Weather Station endpoint.
    Receives a dummy input 'user_input' to enable dataflow node triggering from upstream nodes.
    Outputs weather data as a JSON-serializable dict on the 'weather_data' port.
    Dependencies: requests
    """
    try:
        # Dummy read to conform to upstream dataflow node structure
        user_input = agent.receive_parameter('user_input')

        endpoint = "https://api.opensensemap.org/boxes/57000b8745fd40c8196ad04c?format=json"
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        
        agent.send_output(
            agent_output_name="weather_data",
            agent_result=weather_data  # Ensure dict for serialization
        )
    except Exception as e:
        # Encapsulate errors into a string output for safe node execution
        agent.send_output(
            agent_output_name="weather_data",
            agent_result={"error": str(e)}
        )

def main():
    agent = MofaAgent(agent_name="SenseboxWeatherStationNode")
    run(agent=agent)

if __name__ == "__main__":
    main()
