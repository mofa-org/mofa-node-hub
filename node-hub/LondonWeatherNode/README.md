# london_weather_node

A Dora-rs node that fetches the current weather for London from wttr.in. This node performs an HTTP GET request to wttr.in, receives weather data in JSON, and outputs the raw weather JSON response. It is suitable for integration in Dora pipelines where real-time weather updates are required.

## Features
- Fetches real-time weather information for London
- Outputs data in JSON for downstream nodes
- Robust error handling with explicit error output

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
    build: pip install -e london_weather_node
    path: london_weather_node
    inputs:
      user_input: input/user_input
    outputs:
      - weather_json
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
  - id: user_input_node
    build: pip install your-user-input-node
    path: your_user_input_node
    outputs:
      - user_input

  - id: weather
    build: pip install -e london_weather_node
    path: london_weather_node
    inputs:
      user_input: user_input_node/user_input
    outputs:
      - weather_json
```

Your point source must output:

* Topic: `user_input`
* Data: Arbitrary (not used by this node, but implemented for compatibility)
* Metadata:

  ```json
  {
    "description": "Any user input. Not used by LondonWeatherNode, but required for pipeline compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type      | Description                          |
|-------------|-----------|--------------------------------------|
| user_input  | Any       | Placeholder input for compatibility.  |

### Output Topics

| Topic        | Type   | Description                                         |
|--------------|--------|-----------------------------------------------------|
| weather_json | JSON   | Raw current weather response (or error if occurred). |

## License

Released under the MIT License.
