from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# Dependencies:
# - requests
#   Install with: pip install requests

@run_agent
def run(agent: MofaAgent):
    """
    Fetches public holidays (feriados) for the current year in Argentina using the public API at https://api.argentinadatos.com/v1/feriados/.
    Receives an optional 'user_input' parameter for compatibility with other nodes.
    Returns the holidays as a list/dict structure via 'feriados_output' port.
    """
    # for node chaining compatibility
    user_input = agent.receive_parameter('user_input')  # (unused)
    endpoint = "https://api.argentinadatos.com/v1/feriados/"
    timeout = 10
    try:
        response = requests.get(endpoint, timeout=timeout)
        response.raise_for_status()
        try:
            feriados = response.json()
        except Exception as json_err:
            agent.send_output(
                agent_output_name='feriados_output',
                agent_result={
                    'error': True,
                    'message': f'JSON parse error: {str(json_err)}',
                    'raw': response.text
                }
            )
            return
        agent.send_output(
            agent_output_name='feriados_output',
            agent_result=feriados
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='feriados_output',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='ArgentinaFeriadosFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
