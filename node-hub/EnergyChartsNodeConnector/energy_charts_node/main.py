from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Input placeholder to allow upstream connections
    user_input = agent.receive_parameter('user_input')
    try:
        # Endpoint 1: Day-ahead spot market price for DE-LU
        endpoint1 = "https://api.energy-charts.info/price?bzn=DE-LU"
        response1 = requests.get(endpoint1)
        response1.raise_for_status()
        data1 = response1.json()

        # Endpoint 2: Public Power Switzerland
        endpoint2 = "https://api.energy-charts.info/public_power?country=ch"
        response2 = requests.get(endpoint2)
        response2.raise_for_status()
        data2 = response2.json()

        # Prepare output structure (all outputs must be serializable)
        processed_data = {
            'day_ahead_price_DE_LU': data1,
            'public_power_CH': data2
        }
    except Exception as e:
        # Error handling: send error details
        processed_data = {
            'error': True,
            'message': str(e)
        }

    agent.send_output(
        agent_output_name='energy_charts_data',
        agent_result=processed_data
    )

def main():
    agent = MofaAgent(agent_name='EnergyChartsNodeConnector')
    run(agent=agent)

if __name__ == '__main__':
    main()
