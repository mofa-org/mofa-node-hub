# weather_forecast_node

A Dora-rs node for retrieving real-time and hourly weather forecasts from the Open-Meteo API using latitude and longitude as parameters. The node returns current temperature, humidity, rain status, weather code, and hourly precipitation/temperature forecasts.

## Features
- Retrieves live weather data using latitude and longitude
- Provides both current weather and hourly weather forecast in structured JSON
- Returns clear error messages for invalid inputs or failed API requests

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
  - id: weather_forecast
    build: pip install -e weather_forecast_node
    path: weather_forecast_node
    inputs:
      latitude: input/latitude
      longitude: input/longitude
    outputs:
      - weather_forecast
      - error
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
  - id: location_provider
    build: pip install your-location-node
    path: location_node
    outputs:
      - latitude
      - longitude
  - id: weather_forecast
    build: pip install -e weather_forecast_node
    path: weather_forecast_node
    inputs:
      latitude: location_provider/latitude
      longitude: location_provider/longitude
    outputs:
      - weather_forecast
      - error
```

Your point source must output:

* Topic: `latitude`, `longitude`
* Data: String representation of latitude and longitude (e.g., "37.7749", "-122.4194")
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Latitude or longitude value as string."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                        |
| ---------- | ------ | ---------------------------------- |
| latitude   | string | Latitude coordinate as a string    |
| longitude  | string | Longitude coordinate as a string   |

### Output Topics

| Topic            | Type   | Description                                          |
| ---------------- | ------ | ---------------------------------------------------- |
| weather_forecast | json   | Combined current and hourly forecast or results      |
| error            | string | Error message if input/processing fails              |

## License

Released under the MIT License.
