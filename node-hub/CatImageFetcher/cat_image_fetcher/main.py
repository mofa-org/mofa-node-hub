from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import os

@run_agent
def run(agent: MofaAgent):
    """
    Fetches random cat images from TheCatAPI.
    If receives an input parameter 'limit', fetches that many images (max capped by API). Otherwise, fetches default_limit from config.
    Outputs the list of image urls as JSON-serializable list.
    """
    # Ensure compatibility with potential caller nodes even if not needed
    user_input = agent.receive_parameter('user_input')
    try:
        # Try to get 'limit' parameter if provided
        try:
            params = agent.receive_parameters(['limit'])
            limit_raw = params.get('limit', None)
        except Exception:
            limit_raw = None
        # Convert to int if possible, else use default
        if limit_raw is not None and len(limit_raw.strip()) > 0:
            try:
                limit = int(limit_raw)
            except ValueError:
                limit = 10  # fallback to default_limit
        else:
            limit = 10

        api_url = 'https://api.thecatapi.com/v1/images/search'
        fetch_url = api_url
        params = {'limit': limit}
        response = requests.get(fetch_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Extract only the image URLs
        image_urls = [item.get('url') for item in data if 'url' in item]

        agent.send_output(
            agent_output_name='cat_image_urls',
            agent_result=image_urls
        )
    except Exception as e:
        agent.send_output(
            agent_output_name='cat_image_urls',
            agent_result={
                'error': 'Failed to fetch cat images',
                'details': str(e)
            }
        )

def main():
    agent = MofaAgent(agent_name='CatImageFetcher')
    run(agent=agent)

if __name__ == '__main__':
    main()
