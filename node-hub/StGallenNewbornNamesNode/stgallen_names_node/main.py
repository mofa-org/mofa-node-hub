from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    try:
        # Inputs: string year (e.g., '1991') and gender ('1'=male, '2'=female) required.
        params = agent.receive_parameters(['year', 'gender'])
        year = params.get('year')  # Expecting 4-digit string year
        gender = params.get('gender')  # '1' for male, '2' for female

        # Validate input
        if year is None or gender is None:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={"error": "Missing year or gender parameter."}
            )
            return

        # Type safety
        year = str(year)
        gender = str(gender)
        if gender not in ('1', '2'):
            agent.send_output(
                agent_output_name='api_response',
                agent_result={"error": "Gender must be '1' (male) or '2' (female)."}
            )
            return

        # Prepare API endpoint
        endpoint_template = (
            "https://daten.sg.ch/api/explore/v2.1/catalog/datasets/vornamen-der-neugeborenen-kanton-stgallen-seit-1987/records"
            "?where=year%20%3E%3D%20'%s-01-01'%%20AND%%20year%%20%%3C%%3D%%20'%s-12-31'%%20AND%%20geschlecht%%20%%3D%s&limit=20"
        )
        url = endpoint_template % (year, year, gender)

        # Call the API
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            try:
                result = response.json()
            except Exception as e:
                agent.send_output(
                    agent_output_name='api_response',
                    agent_result={"error": f"Invalid JSON from API: {str(e)}"}
                )
                return
            agent.send_output(
                agent_output_name='api_response',
                agent_result=result
            )
        else:
            agent.send_output(
                agent_output_name='api_response',
                agent_result={"error": f"API returned status code {response.status_code}"}
            )
    except Exception as e:
        agent.send_output(
            agent_output_name='api_response',
            agent_result={"error": f"Agent error: {str(e)}"}
        )

def main():
    agent = MofaAgent(agent_name='StGallenNewbornNamesNode')
    run(agent=agent)

if __name__ == '__main__':
    main()

# Dependencies: requests
# Dataflow input ports: 'year', 'gender' (both str, required)
# Dataflow output port: 'api_response' (dict/str)