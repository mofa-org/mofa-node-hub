# dependencies: requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Always receive a user_input to allow dataflow from upstream nodes
        user_input = agent.receive_parameter('user_input')  # stateless input support
        
        # Receive 'text' parameter for logo generation
        text = agent.receive_parameter('text')
        if not text:
            # Fallback to default if not provided
            text = "Abhi Api"
        
        # Construct API call
        endpoint = "https://abhi-api.vercel.app/api/logo/glitch"
        params = {'text': text}
        response = requests.get(endpoint, params=params, timeout=10)
        
        # Check response
        if response.status_code == 200:
            # The API likely returns an image or image URL; handle accordingly
            result_data = {
                'glitch_logo_url': response.url,  # Final URL for the logo image
                'status': 'success',
                'input_text': text
            }
        else:
            result_data = {
                'status': 'error',
                'message': f'API returned status {response.status_code}',
                'input_text': text
            }
        
        agent.send_output(
            agent_output_name='glitch_logo_result',
            agent_result=result_data
        )
    except Exception as e:
        error_result = {
            'status': 'error',
            'message': str(e)
        }
        agent.send_output(
            agent_output_name='glitch_logo_result',
            agent_result=error_result
        )

def main():
    agent = MofaAgent(agent_name='GlitchEffectLogoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
