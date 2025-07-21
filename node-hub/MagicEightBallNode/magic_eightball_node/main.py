from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies: requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive 'mode': 'random' or 'biased'.
        params = agent.receive_parameters(['mode', 'question'])
        mode = params.get('mode', 'random').strip().lower()  # default 'random'
        question = params.get('question', None)
        response_data = None
        
        if mode == 'random':
            resp = requests.get('https://eightballapi.com/api', timeout=10)
            resp.raise_for_status()
            response_data = resp.json()
        elif mode == 'biased':
            if not question:
                agent.send_output(
                    agent_output_name='eightball_response',
                    agent_result={
                        'error': 'question parameter required for biased mode.'
                    }
                )
                return
            headers = {'Content-Type': 'application/json'}
            payload = {'question': question}
            resp = requests.post(
                'https://eightballapi.com/api/biased',
                headers=headers,
                json=payload,
                timeout=10
            )
            resp.raise_for_status()
            response_data = resp.json()
        else:
            agent.send_output(
                agent_output_name='eightball_response',
                agent_result={
                    'error': f"Unsupported mode: {mode}"}
            )
            return
        # Output must be serializable.
        agent.send_output(
            agent_output_name='eightball_response',
            agent_result=response_data
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='eightball_response',
            agent_result={
                'error': f"Exception: {str(e)}"
            }
        )

def main():
    agent = MofaAgent(agent_name='MagicEightBallNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
