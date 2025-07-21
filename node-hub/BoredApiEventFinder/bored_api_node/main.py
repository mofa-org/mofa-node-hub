from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    BoredApiEventFinder
    Provides three functionalities:
    1. Finds an event with a specified price range (minprice, maxprice required)
    2. Finds a random event for a given number of participants (participants required)
    3. Gets a completely random event (no parameters required)
    The function determines which endpoint to hit based on received parameters.
    """
    try:
        # Receive all possible parameter inputs as strings
        params = agent.receive_parameters(['minprice', 'maxprice', 'participants', 'mode', 'user_input'])

        mode = params.get('mode', '').strip().lower()  # mode: 'price', 'participants', 'random'
        minprice = params.get('minprice')
        maxprice = params.get('maxprice')
        participants = params.get('participants')

        if mode == 'price':
            # Price-constrained event
            try:
                min_val = float(minprice) if minprice is not None else 0
                max_val = float(maxprice) if maxprice is not None else 10
            except ValueError:
                return agent.send_output('error', {'error': 'Invalid minprice/maxprice. Must be numbers.'})
            endpoint = f"http://www.boredapi.com/api/activity?minprice={min_val}&maxprice={max_val}"
        elif mode == 'participants':
            try:
                p_num = int(participants) if participants is not None else 3
            except ValueError:
                return agent.send_output('error', {'error': 'Invalid participants. Must be an integer.'})
            endpoint = f"http://www.boredapi.com/api/activity?participants={p_num}"
        else:
            # 'random' or default
            endpoint = "http://www.boredapi.com/api/activity/"
            # For statelessness and compatibility, always allow receiving 'user_input'
            _ = params.get('user_input')  # To facilitate calling by other nodes

        res = requests.get(endpoint, timeout=8)
        if res.status_code == 200:
            # Ensure output is serializable
            agent.send_output(
                agent_output_name='api_event',
                agent_result=res.json()
            )
        else:
            agent.send_output(
                agent_output_name='error',
                agent_result={'error': f'API request failed: {res.status_code}'}
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='error',
            agent_result={'error': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='BoredApiEventFinder')
    run(agent=agent)

if __name__ == '__main__':
    main()
