from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Even though the endpoints require no parameters, to facilitate downstream node calling:
    user_input = agent.receive_parameter('user_input')  # Accepts string, can be empty or ignored
    endpoints = {
        'episodes': 'https://api.sampleapis.com/avatar/episodes',
        'characters': 'https://api.sampleapis.com/avatar/characters',
        'info': 'https://api.sampleapis.com/avatar/info',
    }

    # Determine which data to fetch based on user_input, default to 'info'
    input_str = str(user_input).strip().lower() if user_input is not None else 'info'
    if input_str not in endpoints:
        input_str = 'info'  # fallback

    url = endpoints[input_str]
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # Try to get json, else text
        try:
            data = response.json()
        except Exception:
            data = response.text
        # Output data (guaranteed serializable)
        agent.send_output(
            agent_output_name=f'{input_str}_data',  # e.g., episodes_data, characters_data, info_data
            agent_result=data
        )
    except Exception as e:
        # error handling, output as str
        agent.send_output(
            agent_output_name='error',
            agent_result=str(e)
        )

def main():
    agent = MofaAgent(agent_name='AvatarApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
