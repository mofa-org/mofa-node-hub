# Dependencies required: requests
# Ensure `requests` is listed as a dependency in your project.

from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Receives user_input for compatibility even though unused
    user_input = agent.receive_parameter('user_input')
    
    outputs = {}
    errors = []
    
    # 1. Get Package Info for 'react'
    try:
        pkg_resp = requests.get('https://registry.npmjs.org/react/', timeout=10)
        pkg_resp.raise_for_status()
        pkg_info = pkg_resp.json()
        outputs['package_info'] = pkg_info
    except Exception as e:
        outputs['package_info'] = None
        errors.append(f"package_info error: {str(e)}")

    # 2. Search for 'react'
    try:
        search_url = 'https://registry.npmjs.org/-/v1/search?text=react'
        search_resp = requests.get(search_url, timeout=10)
        search_resp.raise_for_status()
        search_info = search_resp.json()
        outputs['search_results'] = search_info
    except Exception as e:
        outputs['search_results'] = None
        errors.append(f"search_results error: {str(e)}")
    
    # Attach errors, if any
    if errors:
        outputs['errors'] = errors
    
    agent.send_output(
        agent_output_name='npm_registry_data',
        agent_result=outputs  # dict is serializable
    )

def main():
    agent = MofaAgent(agent_name='NpmRegistryNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
