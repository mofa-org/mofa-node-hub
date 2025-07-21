from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    # Input added to comply with framework integration; ignored as API needs no input
    user_input = agent.receive_parameter('user_input')
    try:
        # Access general municipal data cubes endpoint
        cubes_response = requests.get("https://municipaldata.treasury.gov.za/api/cubes", timeout=10)
        cubes_response.raise_for_status()
        cubes_data = cubes_response.json()

        # Access repairs and maintenance model endpoint
        repmaint_response = requests.get("https://municipaldata.treasury.gov.za/api/cubes/repmaint/model", timeout=10)
        repmaint_response.raise_for_status()
        repmaint_data = repmaint_response.json()

        # Package output as a dictionary
        output_data = {
            "cubes": cubes_data,
            "repairs_maintenance_model": repmaint_data
        }
        agent.send_output(
            agent_output_name='municipal_financial_data',
            agent_result=output_data
        )
    except Exception as e:
        # Ensure errors are contained and output is serializable
        error_output = {
            "error": True,
            "message": str(e)
        }
        agent.send_output(
            agent_output_name='municipal_financial_data',
            agent_result=error_output
        )

def main():
    agent = MofaAgent(agent_name='MunicipalFinancialDataNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
