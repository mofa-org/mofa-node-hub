from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests

@run_agent
def run(agent: MofaAgent):
    """
    HeatStressWarningNode fetches Heat Stress at Work Warnings from Hong Kong Observatory in specified language.
    Input:
        lang: str - one of 'en', 'tc', 'sc' for English, Traditional or Simplified Chinese.
    Output:
        warning_data: dict or str - Serializable JSON from the weather API
    """
    try:
        # Input handling: receive language selection
        lang = agent.receive_parameter('lang')
        # Type safety and validation
        if not isinstance(lang, str):
            raise ValueError("Input parameter 'lang' must be a string.")
        lang = lang.strip().lower()

        # Map valid language codes
        lang_map = {'en': 'en', 'tc': 'tc', 'sc': 'sc'}
        if lang not in lang_map:
            agent.send_output('warning_data', {'error': f"Invalid lang value: '{lang}'. Must be one of 'en', 'tc', 'sc'."})
            return

        # Define endpoint according to lang
        base_url = "https://data.weather.gov.hk/weatherAPI/opendata/hsww.php"
        endpoint = f"{base_url}?lang={lang_map[lang]}"

        # Outgoing GET request
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except Exception:
            # Fallback to text
            data = response.text

        agent.send_output(
            agent_output_name='warning_data',
            agent_result=data
        )
    except Exception as e:
        # Output error as serializable dict
        agent.send_output('warning_data', {'error': str(e)})

def main():
    agent = MofaAgent(agent_name='HeatStressWarningNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
