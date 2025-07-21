from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

# FederalRegisterDocumentNode dependencies:
#   - requests
#     (Install: pip install requests)

API_BASE_URL = "https://www.federalregister.gov/api/v1"
DEFAULT_PUBLICATION_DATE = "2023-03-14"
REQUEST_TIMEOUT = 10

def fetch_single_document(document_id: str, publication_date: str = DEFAULT_PUBLICATION_DATE):
    try:
        endpoint = f"{API_BASE_URL}/documents/{document_id}?publication_date={publication_date}"
        response = requests.get(endpoint, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

def fetch_all_documents():
    try:
        endpoint = f"{API_BASE_URL}/documents"
        response = requests.get(endpoint, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

@run_agent
def run(agent: MofaAgent):
    try:
        # Determine operation type based on parameters. If no parameter, fetch all documents.
        params = agent.receive_parameters(['document_id', 'publication_date'])
        document_id = params.get('document_id')
        publication_date = params.get('publication_date')

        if document_id and document_id.strip():
            # Fetch single document
            if not publication_date or not publication_date.strip():
                publication_date = DEFAULT_PUBLICATION_DATE
            result = fetch_single_document(document_id=document_id.strip(), publication_date=publication_date.strip())
            agent.send_output(
                agent_output_name='single_document',
                agent_result=result
            )
        else:
            # If no document_id given, fetch all documents
            result = fetch_all_documents()
            agent.send_output(
                agent_output_name='all_documents',
                agent_result=result
            )
    except Exception as exc:
        agent.send_output(
            agent_output_name='error',
            agent_result={"error": str(exc)}
        )

def main():
    agent = MofaAgent(agent_name='FederalRegisterDocumentNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
