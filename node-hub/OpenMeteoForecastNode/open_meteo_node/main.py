# Required dependencies: requests (install with `pip install requests`)
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
import requests
import json

@run_agent
def run(agent: MofaAgent):
    # Receive all parameters as strings (may be missing for default use)
    params = agent.receive_parameters([
        'latitude',
        'longitude',
        'daily',
        'hourly',
        'current',
        'timezone'
    ])

    try:
        # Defaults (Berlin, match config)
        endpoint = "https://api.open-meteo.com/v1/forecast"
        query_params = {
            'latitude': params.get('latitude') or '52.52',
            'longitude': params.get('longitude') or '13.41',
            'timezone': params.get('timezone') or 'auto',
        }

        # Handle list parameters, allow comma-separated strings as input
        def parse_list_param(param, default):
            val = params.get(param)
            if val:
                if isinstance(val, str):
                    return val
                if isinstance(val, list):
                    return ','.join(val)
            return ','.join(default)

        # Set default values as in config.yaml
        default_daily = [
            "weather_code", "temperature_2m_max", "temperature_2m_min", "apparent_temperature_max", "apparent_temperature_min",
            "wind_speed_10m_max", "sunrise", "sunset", "daylight_duration", "sunshine_duration",
            "uv_index_max", "uv_index_clear_sky_max", "rain_sum", "showers_sum", "snowfall_sum", "precipitation_hours",
            "precipitation_sum", "precipitation_probability_max", "wind_gusts_10m_max", "wind_direction_10m_dominant",
            "shortwave_radiation_sum", "et0_fao_evapotranspiration"
        ]
        default_hourly = [
            "temperature_2m", "relative_humidity_2m", "dew_point_2m", "apparent_temperature", "precipitation_probability",
            "precipitation", "rain", "showers", "snowfall", "snow_depth", "vapour_pressure_deficit", "et0_fao_evapotranspiration",
            "visibility", "evapotranspiration", "cloud_cover_high", "cloud_cover_mid", "cloud_cover_low", "cloud_cover",
            "surface_pressure", "pressure_msl", "weather_code", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m",
            "wind_speed_180m", "wind_direction_10m", "wind_direction_80m", "wind_direction_120m", "wind_direction_180m",
            "wind_gusts_10m", "temperature_80m", "temperature_120m", "temperature_180m", "soil_temperature_0cm",
            "soil_temperature_6cm", "soil_temperature_18cm", "soil_temperature_54cm", "soil_moisture_0_to_1cm",
            "soil_moisture_1_to_3cm", "soil_moisture_3_to_9cm", "soil_moisture_9_to_27cm", "soil_moisture_27_to_81cm"
        ]
        default_current = [
            "temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "wind_speed_10m",
            "wind_direction_10m", "wind_gusts_10m", "precipitation", "rain", "showers", "snowfall",
            "weather_code", "cloud_cover", "pressure_msl", "surface_pressure"
        ]

        query_params['daily'] = parse_list_param('daily', default_daily)
        query_params['hourly'] = parse_list_param('hourly', default_hourly)
        query_params['current'] = parse_list_param('current', default_current)

        # Call weather API
        response = requests.get(endpoint, params=query_params, timeout=10)
        if response.status_code == 200:
            weather_data = response.json()
            agent.send_output(
                agent_output_name='weather_forecast',
                agent_result=weather_data
            )
        else:
            error_msg = {
                'error': True,
                'status_code': response.status_code,
                'body': response.text[:500]
            }
            agent.send_output(
                agent_output_name='weather_forecast',
                agent_result=error_msg
            )
    except Exception as ex:
        agent.send_output(
            agent_output_name='weather_forecast',
            agent_result={'error': True, 'message': str(ex)}
        )

def main():
    agent = MofaAgent(agent_name='OpenMeteoForecastNode')
    run(agent=agent)

if __name__ == '__main__':
    main()
