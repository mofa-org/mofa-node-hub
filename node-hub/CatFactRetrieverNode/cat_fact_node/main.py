from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Input facilitation for dataflow compliance
        user_input = agent.receive_parameter('user_input')
        
        # API call to fetch a random cat fact
        response = requests.get('https://cat-fact.herokuapp.com/facts/random?amount=1', timeout=10)
        response.raise_for_status()  # Check HTTP errors
        data = response.json()

        # The API returns either a dict (single) or a list (multiple); here, it is a single dict
        if isinstance(data, dict):
            cat_fact = data.get('text', 'No fact found.')
        elif isinstance(data, list) and data:
            cat_fact = data[0].get('text', 'No fact found.')
        else:
            cat_fact = 'No cat fact found.'

        # Output serialization (string)
        agent.send_output(
            agent_output_name='cat_fact',
            agent_result=cat_fact
        )
    except Exception as e:
        # Error handling and serialization
        agent.send_output(
            agent_output_name='cat_fact',
            agent_result=f'Error retrieving cat fact: {str(e)}'
        )

def main():
    agent = MofaAgent(agent_name='CatFactRetrieverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
