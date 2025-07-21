# Dependencies:
#   requests
#   (Ensure requests is listed in your requirements. Configure endpoint through YAML as needed.)

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    """
    Agent that resolves and calculates math functions with variables using the oglimmer API.
    Inputs:
      - expression: str (e.g. '3+4*x')
      - x: str or float convertible (e.g. '5')
      Output on port 'calculation_result':
        API result or error info (dict)
    """
    # Receive and validate input parameters (all as string)
    try:
        params = agent.receive_parameters(['expression', 'x'])  # {'expression': ..., 'x': ...}
        # Type conversion - x should be numeric
        expression = str(params.get('expression', ''))
        x_raw = params.get('x', '')
        try:
            # try to parse x as float
            x_val = float(x_raw)
        except (ValueError, TypeError):
            raise ValueError(f"Parameter 'x' must be numeric, got: {x_raw}")
    except Exception as e:
        # Contained error reporting
        agent.send_output(
            agent_output_name='calculation_result',
            agent_result={
                'success': False,
                'error': f'Input error: {str(e)}'
            }
        )
        return

    # Prepare request
    try:
        endpoint = "https://math.oglimmer.de/v1/calc"  # Configurable if needed
        # Build query string as per API docs
        query = {
            'expression': expression,
            'x': f"x={x_val}"
        }
        resp = requests.get(endpoint, params=query, timeout=8)
        resp.raise_for_status()
        api_result = resp.json() if resp.content else {'result': None}
        agent.send_output(
            agent_output_name='calculation_result',
            agent_result=api_result if isinstance(api_result, (dict, list)) else str(api_result)
        )
    except Exception as ex:
        # API error containment
        agent.send_output(
            agent_output_name='calculation_result',
            agent_result={
                'success': False,
                'error': f'API request error: {str(ex)}'
            }
        )

def main():
    agent = MofaAgent(agent_name='MathFunctionResolverNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
