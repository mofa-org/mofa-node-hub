from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Always receive 'user_input' param for compatibility, even if not used directly
        user_input = agent.receive_parameter('user_input')
        text = agent.receive_parameter('text')  # Input: the text to render in neon style
        
        # Validate input (API expects non-empty 'text')
        if not isinstance(text, str) or not text.strip():
            agent.send_output(
                agent_output_name='logo_url',
                agent_result={
                    'error': True,
                    'message': 'Input parameter "text" must be a non-empty string.'
                }
            )
            return

        # Build NEON LOGO API URL
        base_url = 'https://abhi-api.vercel.app/api/logo/neon'
        params = {'text': text}
        try:
            response = requests.get(base_url, params=params, timeout=15)
        except Exception as ex:
            agent.send_output(
                agent_output_name='logo_url',
                agent_result={'error': True, 'message': f'Request failed: {str(ex)}'}
            )
            return
        if response.status_code == 200 and response.url:
            # The API returns an image url in .url property
            agent.send_output(
                agent_output_name='logo_url',
                agent_result={
                    'error': False,
                    'logo_url': response.url  # This is a direct link to the rendered neon text PNG
                }
            )
        else:
            agent.send_output(
                agent_output_name='logo_url',
                agent_result={
                    'error': True,
                    'status_code': response.status_code,
                    'message': 'Failed to generate neon logo.'
                }
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='logo_url',
            agent_result={'error': True, 'message': f'Unhandled error: {str(e)}'}
        )

def main():
    agent = MofaAgent(agent_name='NeonTextLogoNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
