from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # To facilitate node linkage even though no input is required
    try:
        response = requests.get('https://countriesnow.space/api/v0.1/countries/population', timeout=15)
        response.raise_for_status()
        data = response.json()
        # Validate output is serializable and dictionary-like
        if not isinstance(data, (dict, list, str)):
            data = str(data)
        # Send output on designated port
        agent.send_output(
            agent_output_name='country_population_data',
            agent_result=data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='country_population_data',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='CountryPopulationRetriever')
    run(agent=agent)

if __name__ == '__main__':
    main()
