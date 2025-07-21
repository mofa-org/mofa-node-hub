from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# No external env dependencies or API keys required for public endpoint
# Dependency: requests (add to requirements.txt)

@run_agent
def run(agent: MofaAgent):
    # No input is required for this node, but accepting 'user_input' for compatibility
    user_input = agent.receive_parameter('user_input')
    api_url = "https://pokemon3d-api.onrender.com/v1/all"
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        # The endpoint returns JSON content, which is serializable
        pokemon_3d_data = response.json()
    except Exception as e:
        # Return error as dict for serialization
        agent.send_output(
            agent_output_name='pokemon_3d_models',
            agent_result={"error": True, "message": str(e)}
        )
        return
    
    agent.send_output(
        agent_output_name='pokemon_3d_models',
        agent_result=pokemon_3d_data
    )

def main():
    agent = MofaAgent(agent_name='Pokemon3DModelNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
