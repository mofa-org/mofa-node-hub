from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    try:
        # Always receive parameter to conform to dora-rs dataflow, even if mocked
        email = agent.receive_parameter('user_input')
        
        # Type check and strip whitespaces
        if not isinstance(email, str):
            raise ValueError('Email parameter must be a string')
        email = email.strip()
        if not email:
            raise ValueError('Email parameter is required')
        
        # API endpoint and params
        endpoint = "http://api.eva.pingutil.com/email"
        params = {'email': email}
        
        response = requests.get(endpoint, params=params, timeout=7)
        response.raise_for_status()
        
        # API returns JSON
        api_result = response.json()
        
        # Validate serialization
        if not isinstance(api_result, (dict, list, str)):
            api_result = str(api_result)
        
        agent.send_output(
            agent_output_name='api_verification_result',
            agent_result=api_result
        )
    except Exception as e:
        # Always return error info in a serializable way
        agent.send_output(
            agent_output_name='api_verification_result',
            agent_result={'error': True, 'message': str(e)}
        )

def main():
    agent = MofaAgent(agent_name='EmailVerificationNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Requirements: requests
# Dependency install: pip install requests
