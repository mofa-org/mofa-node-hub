# worldtime_api_node

Real-time WorldTime API Fetcher Dora Node

## Features
- Queries multiple WorldTime API endpoints in parallel for time information.
- Robust error handling for HTTP/network issues and JSON parsing.
- Integrates as a Dora node and responds to parameter requests from other nodes.

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
  - id: worldtime_node
    build: pip install -e .
    path: worldtime_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - worldtime_api_results
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
    build: pip install -e .
    path: your_input_node
    outputs:
      - user_input
  - id: worldtime_node
    build: pip install -e .
    path: worldtime_api_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - worldtime_api_results
```

Your point source must output:

* Topic: `user_input`
* Data: String, number, or JSON-serializable data (determined by your application)
* Metadata:

  ```json
  {
    "type": "parameter",
    "description": "Input parameter for WorldTimeApiNode."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type      | Description                                   |
| ----------- | --------- | --------------------------------------------- |
| user_input  | parameter | Parameter value to trigger/dynamically interact with API call |

### Output Topics

| Topic                 | Type    | Description                                                      |
| --------------------- | ------- | ---------------------------------------------------------------- |
| worldtime_api_results | json    | Time API results or error information for each endpoint queried  |


## License

Released under the MIT License.
