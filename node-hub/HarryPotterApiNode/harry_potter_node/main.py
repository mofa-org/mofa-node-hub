from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Dummy input for dora-rs interface compliance, enables connection with other agents
    user_input = agent.receive_parameter('user_input')

    outputs = {}
    endpoints = {
        'all_spells': 'https://hp-api.onrender.com/api/spells',
        'ravenclaw_characters': 'https://hp-api.onrender.com/api/characters/house/ravenclaw',
        'staff_characters': 'https://hp-api.onrender.com/api/characters/staff',
        'all_characters': 'https://hp-api.onrender.com/api/characters',
    }

    for key, url in endpoints.items():
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            # Validate response serializability (expecting JSON array/list of dicts)
            data = resp.json()
            outputs[key] = data if isinstance(data, (list, dict)) else str(data)
        except Exception as e:
            outputs[key] = {'error': f'Failed to fetch from {url}', 'details': str(e)}

    # Send all outputs at their respective ports
    for out_port, result in outputs.items():
        agent.send_output(
            agent_output_name=out_port,
            agent_result=result
        )

def main():
    agent = MofaAgent(agent_name='HarryPotterApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
