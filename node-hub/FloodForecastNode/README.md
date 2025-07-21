# flood_forecast_node

Real-time river flood forecast integration using Open-Meteo Flood API.

## Features
- Fetches up-to-date river discharge predictions from the Open-Meteo Flood API
- Parameterized geolocation and forecast variables via node inputs
- Robust error reporting via result outputs

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
  - id: flood_forecast
    build: pip install -e flood_forecast_node
    path: flood_forecast_node
    inputs:
      latitude: input/latitude
      longitude: input/longitude
      daily: input/daily
    outputs:
      - flood_forecast
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
  - id: geo_source
    build: pip install your-geosource
    path: your-geosource
    outputs:
      - latitude
      - longitude
      - daily
  - id: flood_forecast
    build: pip install -e flood_forecast_node
    path: flood_forecast_node
    inputs:
      latitude: geo_source/latitude
      longitude: geo_source/longitude
      daily: geo_source/daily
    outputs:
      - flood_forecast
```

Your point source must output:

* Topic: `latitude`, `longitude`, `daily`
* Data: String (for latitude/longitude convertible to float, daily as desired variable)
* Metadata:

  ```json
  {
    "description": "Geolocation and forecast variable for flood prediction",
    "fields": [
      {"name": "latitude", "type": "string"},
      {"name": "longitude", "type": "string"},
      {"name": "daily", "type": "string"}
    ]
  }
  ```

## API Reference

### Input Topics

| Topic     | Type   | Description                         |
|-----------|--------|-------------------------------------|
| latitude  | string | Latitude (as string, cast to float) |
| longitude | string | Longitude (as string, cast to float)|
| daily     | string | Daily variable (e.g. river_discharge)|

### Output Topics

| Topic          | Type      | Description                                            |
|--------------- |-----------|--------------------------------------------------------|
| flood_forecast | JSON dict | Open-Meteo flood forecast result or error structure    |

## License

Released under the MIT License.
