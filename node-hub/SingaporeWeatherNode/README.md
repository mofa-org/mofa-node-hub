# singapore_weather

A Dora-rs node that fetches real-time air temperature data from Singapore's public environmental API (data.gov.sg) and provides it to connected Dora nodes via messaging.

## Features
- Retrieves latest air temperature responses from Singapore’s official data.gov.sg API
- Publishes data with serializable error messages on failure
- Allows integration and triggering via Dora messages (e.g., user input, triggers)

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
  - id: singapore_weather
    build: pip install -e .
    path: singapore_weather
    inputs:
      user_input: input/user_input
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
  - id: your_trigger_node
    build: pip install your-trigger-node
    path: your-trigger-node
    outputs:
      - user_input

  - id: singapore_weather
    build: pip install -e .
    path: singapore_weather
    inputs:
      user_input: your_trigger_node/user_input
    outputs:
      - weather_data

  - id: consumer_node
    build: pip install your-consumer
    path: your-consumer
    inputs:
      weather_data: singapore_weather/weather_data
```

Your point source must output:

* Topic: `user_input`
* Data: String or any trigger content (can be empty if not needed)
* Metadata:

  ```json
  {
    "description": "Input data or trigger message to prompt API fetch."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                        |
| ---------- | ------ | ---------------------------------- |
| user_input | any    | Triggers a weather API fetch event |

### Output Topics

| Topic        | Type   | Description                                      |
| ------------ | ------ | ------------------------------------------------ |
| weather_data | object | JSON dict containing latest air temperature data |


## License

Released under the MIT License.
