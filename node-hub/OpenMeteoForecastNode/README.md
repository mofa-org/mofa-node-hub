# open_meteo_node

Weather forecasting Dora node powered by Open-Meteo API.

## Features
- Real-time weather forecast via Open-Meteo REST API
- Configurable forecast parameters (location, fields, time granularity)
- Reports forecast as structured output for downstream processing

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
```

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: openmeteo
    build: pip install -e .
    path: open_meteo_node
    inputs: []
    outputs:
      - weather_forecast
    params:
      latitude: 52.52
      longitude: 13.41
      timezone: 'auto'
      daily:
        - weather_code
        - temperature_2m_max
        - temperature_2m_min
      hourly:
        - temperature_2m
        - precipitation
      current:
        - temperature_2m
        - wind_speed_10m
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
  - id: openmeteo
    build: pip install -e .
    path: open_meteo_node
    inputs:
      - your_trigger_topic
    outputs:
      - weather_forecast
```

Your point source must output:

* Topic: `your_trigger_topic`
* Data: any (the weather node only fetches when triggered)
* Metadata:

  ```json
  {
    "trigger": true
  }
  ```

## API Reference

### Input Topics

| Topic              | Type               | Description        |
| ------------------ | ------------------ | ------------------ |
| latitude           | string/float       | Latitude for forecast (default: 52.52) |
| longitude          | string/float       | Longitude for forecast (default: 13.41) |
| daily              | string/list[string]| Daily keys to request (see Open-Meteo docs) |
| hourly             | string/list[string]| Hourly keys to request |
| current            | string/list[string]| Current values to request |
| timezone           | string             | Report timezone (default: 'auto') |

### Output Topics

| Topic               | Type                | Description         |
| ------------------- | ------------------- | ------------------- |
| weather_forecast    | dict (JSON)         | Result object from Open-Meteo API or error details |


## License

Released under the MIT License.
