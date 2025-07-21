# Dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate downstream compatibility
    user_input = agent.receive_parameter('user_input')
    try:
        response = requests.get('https://pokefacts.vercel.app/')
        # We expect a JSON response with a Pokemon fact
        if response.status_code == 200:
            try:
                fact = response.json().get('fact', '')
                if not isinstance(fact, str):
                    fact = str(fact)
                agent.send_output(
                    agent_output_name='pokemon_fact',
                    agent_result=fact
                )
            except Exception as json_err:
                agent.send_output(
                    agent_output_name='pokemon_fact',
                    agent_result=f"Error parsing JSON response: {json_err}"
                )
        else:
            agent.send_output(
                agent_output_name='pokemon_fact',
                agent_result=f"API Error: Status code {response.status_code}"
            )
    except Exception as err:
        agent.send_output(
            agent_output_name='pokemon_fact',
            agent_result=f"Request Exception: {err}"
        )

def main():
    agent = MofaAgent(agent_name='PokemonFactProvider')
    run(agent=agent)

if __name__ == '__main__':
    main()
