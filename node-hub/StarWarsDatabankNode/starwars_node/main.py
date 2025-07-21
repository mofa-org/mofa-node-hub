from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Add this line to facilitate calls from other nodes, even though no input is required
    user_input = agent.receive_parameter('user_input')

    # Endpoints dictionary for Star Wars Databank API
    endpoints = {
        'locations': 'https://starwars-databank-server.vercel.app/api/v1/locations',
        'characters': 'https://starwars-databank-server.vercel.app/api/v1/characters',
        'droids': 'https://starwars-databank-server.vercel.app/api/v1/droids',
    }
    result = {}
    try:
        for key, url in endpoints.items():
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                # Each API returns JSON
                result[key] = resp.json()
            except Exception as e:
                result[key] = {'error': str(e)}
    except Exception as e:
        result = {'error': f'Unexpected agent-level error: {str(e)}'}

    # Ensure the output is serializable
    agent.send_output(
        agent_output_name='starwars_api_data',
        agent_result=result
    )

def main():
    agent = MofaAgent(agent_name='StarWarsDatabankNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
