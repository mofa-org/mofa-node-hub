# weather_data_node

Fetch real-time weather data for any location using OpenWeatherMap, as a Dora-rs node.

## Features
- Get current weather for any city/location
- Graceful error handling with informative messages
- Easily integrates with other Dora/MoFa nodes via parameters

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
  - id: weather_data_node
    build: pip install -e .
    path: weather_data_node
    inputs:
      location: input/location
      user_input: input/user_input
    outputs:
      - weather_data
    env:
      OPENWEATHER_API_KEY: "<your-api-key>"
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
  - id: location_source
    build: pip install your-location-source
    path: your-location-source
    outputs:
      - location
      - user_input
  - id: weather_data_node
    build: pip install -e .
    path: weather_data_node
    inputs:
      location: location_source/location
      user_input: location_source/user_input
    outputs:
      - weather_data
```

Your point source must output:

* Topic: `location`, `user_input`
* Data: For location: (string, e.g. "Berlin"), for user_input: any (typically a string)
* Metadata:

  ```json
  {
    "dtype": "string"  // For location
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                    |
|------------|--------|------------------------------------------------|
| location   | string | Name of the location/city to fetch weather for |
| user_input | any    | Dummy parameter, can be used for triggering    |

### Output Topics

| Topic        | Type | Description                              |
|--------------|------|------------------------------------------|
| weather_data | dict | Weather information or error message JSON |

## License

Released under the MIT License.
