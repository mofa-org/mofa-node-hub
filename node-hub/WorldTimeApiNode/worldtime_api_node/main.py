from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    user_input = agent.receive_parameter('user_input')  # To facilitate other nodes to call

    endpoints = {
        'europe': 'http://worldtimeapi.org/api/timezone/Europe',
        'argentina_salta': 'http://worldtimeapi.org/api/timezone/America/Argentina/Salta',
        'ip_8_8_8_8': 'http://worldtimeapi.org/api/ip/8.8.8.8'
    }

    results = {}
    try:
        for key, url in endpoints.items():
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    # Attempt to parse as JSON, fallback to raw text
                    try:
                        results[key] = response.json()
                    except Exception:
                        results[key] = response.text
                else:
                    results[key] = {'error': f'HTTP {response.status_code}'}
            except Exception as e:
                results[key] = {'error': str(e)}
    except Exception as major_e:
        results = {'error': f'Critical error occurred: {str(major_e)}'}

    # Ensure result is serializable
    try:
        serializable_output = json.loads(json.dumps(results))
    except Exception as e:
        serializable_output = {'error': f'Serialization failed: {str(e)}'}

    agent.send_output(
        agent_output_name='worldtime_api_results',
        agent_result=serializable_output
    )

def main():
    agent = MofaAgent(agent_name='WorldTimeApiNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
