from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Facilitate calls from other nodes for compatibility
    user_input = agent.receive_parameter('user_input')

    results = {}
    try:
        # Get EC2 prices/specs
        ec2_url = "https://ec2.shop/?json"
        ec2_resp = requests.get(ec2_url, timeout=15)
        ec2_resp.raise_for_status()
        results['ec2'] = ec2_resp.json()
    except Exception as e:
        results['ec2'] = {'error': str(e)}

    try:
        # Get RDS prices
        rds_url = "https://ec2.shop/rds?json"
        rds_resp = requests.get(rds_url, timeout=15)
        rds_resp.raise_for_status()
        results['rds'] = rds_resp.json()
    except Exception as e:
        results['rds'] = {'error': str(e)}

    # Output delivery, serialization enforced
    agent.send_output(
        agent_output_name='aws_pricing_output',
        agent_result=results
    )

def main():
    agent = MofaAgent(agent_name='AwsPricingNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies:
#   - requests

# This agent fetches AWS EC2 and RDS pricing/specifications.
# Uses only GETs and public endpoints; no API key required.