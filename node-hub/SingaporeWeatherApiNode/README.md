# singapore_weather_api

Real-time Singapore Weather Data Dora Node

## Features
- Fetches real-time rainfall, UV index, and 24-hour weather forecast from data.gov.sg
- Provides easy integration into Dora/Mofa pipelines
- Supports filtering by specific data type (rainfall, uv, or forecast)

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: singapore_weather
    build: pip install -e .
    path: singapore_weather_api
    inputs:
      user_input: input/user_input # (optional) triggers API call
      data_type: input/data_type   # (optional) "rainfall", "uv", or "forecast"
    outputs:
      - singapore_weather_data
```

Run the demo:

```bash
dora build demo.yml
dora start demo.yml
```


## Integration with Other Nodes

To connect with your existing node:

```yaml
nodes:
  - id: my_custom_trigger
    build: pip install my-custom-trigger
    path: my_custom_trigger
    outputs:
      - user_input

  - id: singapore_weather
    build: pip install -e .
    path: singapore_weather_api
    inputs:
      user_input: my_custom_trigger/user_input
      data_type: input/data_type  # Optional, specify if needed
    outputs:
      - singapore_weather_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (dummy trigger or None)
* Metadata:

  ```json
  {
    "description": "Trigger to cause Singapore weather API node to fetch data. Payload is unused."
  }
  ```

## API Reference

### Input Topics

| Topic         | Type    | Description                             |
| -------------|---------|-----------------------------------------|
| user_input    | any     | Dummy input to trigger data pull        |
| data_type     | string  | 'rainfall', 'uv', 'forecast' (optional) |

### Output Topics

| Topic                  | Type               | Description                                          |
|------------------------|--------------------|------------------------------------------------------|
| singapore_weather_data | dict (JSON object) | Real-time Sg weather data (rainfall, uv, forecast)   |
|                        |                    | Contains top-level keys: 'rainfall', 'uv', 'forecast'|


## License

Released under the MIT License.

````