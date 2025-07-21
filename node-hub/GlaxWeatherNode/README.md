# glax_weather_node

A Dora-rs node for real-time weather data retrieval using the public glax_weather API. Supports configurable location input, units, and toggles for current or forecasted weather.

## Features
- Fetches current or hourly weather data for any location
- Configurable input: city name, longitude/latitude, units, and forecast flag
- Clean Dora dataflow output as a JSON dictionary

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
  - id: weather
    build: pip install -e glax_weather_node  # install this node
    path: glax_weather_node
    inputs:
      location: input/location
      lon: input/lon
      lat: input/lat
      units: input/units
      forecast: input/forecast
    outputs:
      - weather_response
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
  - id: my_inputs
    # Your source node
    outputs:
      - location
      - lon
      - lat
      - units
      - forecast
  - id: weather
    build: pip install -e glax_weather_node
    path: glax_weather_node
    inputs:
      location: my_inputs/location
      lon: my_inputs/lon
      lat: my_inputs/lat
      units: my_inputs/units
      forecast: my_inputs/forecast
    outputs:
      - weather_response
```

Your point source must output:

* Topic: `location`, `lon`, `lat`, `units`, `forecast`
* Data: String values (for each parameter)
* Metadata:

  ```json
  {
    "type": "str",
    "desc": "User-selected or programmatically-set string (city/location, coordinate, etc.)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type | Description                                |
| ---------- | ---- | ------------------------------------------ |
| location   | str  | City or location name                      |
| lon        | str  | Longitude as string (e.g., '7.4474')       |
| lat        | str  | Latitude as string (e.g., '46.9481')       |
| units      | str  | 'metric', 'imperial', or API-defined units |
| forecast   | str  | 'on', 'off', 'true', 'false', etc.         |

### Output Topics

| Topic            | Type         | Description                                     |
| --------------- | ------------ | ----------------------------------------------- |
| weather_response | Dict (JSON)  | Dictionary result from glax_weather API call    |

## License

Released under the MIT License.
