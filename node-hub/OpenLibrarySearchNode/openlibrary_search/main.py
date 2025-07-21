# Dependencies: requests
# To install: pip install requests
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

def search_books_by_title(title: str):
    try:
        url = f"https://openlibrary.org/search.json?title={requests.utils.quote(title)}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data
    except Exception as e:
        return {"error": True, "message": str(e)}

def search_books_by_author(author: str, sort: str = None):
    try:
        url = f"https://openlibrary.org/search.json?author={requests.utils.quote(author)}"
        if sort:
            url += f"&sort={requests.utils.quote(sort)}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data
    except Exception as e:
        return {"error": True, "message": str(e)}

@run_agent
def run(agent: MofaAgent):
    # Receive operation type and query parameters
    # Possible operations: 'title_search', 'author_search'
    params = agent.receive_parameters(['operation', 'query', 'sort'])  # all string
    operation = params.get('operation', '').strip().lower()
    query = params.get('query', '').strip()
    sort = params.get('sort')  # can be None

    result = None

    if operation == 'title_search':
        if not query:
            result = {"error": True, "message": "Missing book title for search."}
        else:
            result = search_books_by_title(query)
    elif operation == 'author_search':
        if not query:
            result = {"error": True, "message": "Missing author name for search."}
        else:
            result = search_books_by_author(query, sort)
    else:
        result = {"error": True, "message": "Invalid operation type. Use 'title_search' or 'author_search'."}

    agent.send_output(
        agent_output_name='openlibrary_results',
        agent_result=result  # dict, always serializable
    )

def main():
    agent = MofaAgent(agent_name='OpenLibrarySearchNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
