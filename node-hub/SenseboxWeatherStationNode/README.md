# sensebox_weather_node

A Dora-rs node that fetches live weather data from the public Sensebox Weather Station API, providing real-time environmental sensor data for downstream Dora pipelines.

## Features
- Live weather data retrieval from Sensebox OpenSenseMap
- Seamless integration as a Dora-rs node for reactive dataflows
- Robust error handling and JSON serialization for easy interop

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
  - id: sensebox_weather_node
    build: pip install -e .
    path: sensebox_weather_node
    inputs:
      user_input: upstream_node/trigger
    outputs:
      - weather_data
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
  - id: upstream_node
    build: pip install your-upstream-node
    path: your-upstream-node
    outputs:
      - trigger
  - id: sensebox_weather_node
    build: pip install -e .
    path: sensebox_weather_node
    inputs:
      user_input: upstream_node/trigger
    outputs:
      - weather_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any primitive value (e.g., string or int) to allow triggering
* Metadata:

  ```json
  {
    "type": "trigger",
    "desc": "Arbitrary value to trigger weather fetch."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                         |
| ---------- | ------- | ----------------------------------- |
| user_input | Any     | Dummy trigger to initiate weather fetch |

### Output Topics

| Topic        | Type  | Description                         |
| ------------ | ------------- | ----------------------------------- |
| weather_data | JSON/dict      | Weather data fetched from Sensebox, or error message |


## License

Released under the MIT License.
