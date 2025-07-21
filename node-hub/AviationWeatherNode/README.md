# aviation_weather_node

Fetches live aviation weather data from the FAA for a requested airport (default: ZRH). Outputs results as JSON or error state, callable as a MofaAgent node.

## Features
- Retrieves up-to-date aviation weather data for a specified airport.
- Handles error conditions gracefully and returns clear error messages.
- Easy integration in Dora/MOFA graphs via input/output topics and Python interface.

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
  - id: aviation_weather
    build: pip install -e aviation_weather_node
    path: aviation_weather_node
    inputs:
      user_input: input/user_input
    outputs:
      - aviation_weather_result
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
  - id: your_input_node
    build: pip install -e your_input_node
    path: your_input_node
    outputs:
      - user_input
  - id: aviation_weather
    build: pip install -e aviation_weather_node
    path: aviation_weather_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - aviation_weather_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable Python object (can be dummy; this node does not use it but expects interface compliance)
* Metadata:

  ```json
  {
    "description": "Placeholder for triggering aviation weather API call"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                         |
| ----------- | ------- | --------------------------------------------------- |
| user_input  | any     | Placeholder input (not used) for trigger/interface. |

### Output Topics

| Topic                   | Type   | Description                                          |
| ----------------------- | ------ | ---------------------------------------------------- |
| aviation_weather_result | dict   | Weather data as returned from the API or error info. |


## License

Released under the MIT License.
