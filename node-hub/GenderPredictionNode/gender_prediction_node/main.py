from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Receive input from dataflow (the name to be predicted)
        name = agent.receive_parameter('name')
        if not isinstance(name, str):
            raise ValueError('Input parameter "name" must be of type str')
        
        # Prepare request parameters
        endpoint = "https://api.genderize.io"
        params = {'name': name}

        # Make the GET request to the Genderize API
        response = requests.get(endpoint, params=params, timeout=8)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse response JSON and serialize it
        result = response.json()
        if not isinstance(result, dict):
            raise ValueError('API response is not a valid dictionary')
        
        # Agent output (must be serializable)
        agent.send_output(
            agent_output_name='gender_prediction',
            agent_result=result
        )
    except Exception as e:
        # Safe error handling: send error message in structured form
        agent.send_output(
            agent_output_name='gender_prediction',
            agent_result={
                'error': True,
                'message': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='GenderPredictionNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests