# spacex_launch_node

Fetch the latest SpaceX launch data from the SpaceX API and expose it in Dora as a streaming node.

## Features
- Retrieves up-to-date data on the latest SpaceX launch
- Exposes data as a dict on a named output topic
- Designed for integration with Dora-based pipelines

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
  - id: spacex_launch_node
    build: pip install -e .
    path: spacex_launch_node
    inputs:
      user_input: orchestrator/user_input  # Required for orchestration compatibility
    outputs:
      - launch_data
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
  - id: spacex_launch_node
    build: pip install -e .
    path: spacex_launch_node
    inputs:
      user_input: orchestrator/user_input
    outputs:
      - launch_data

  - id: my_consumer_node
    build: pip install my-consumer-node
    path: my_consumer_node
    inputs:
      launch_data: spacex_launch_node/launch_data
```

Your point source must output:

* Topic: `launch_data`
* Data: Dictionary containing SpaceX launch data as returned by the SpaceX v5 launches/latest API
* Metadata:

  ```json
  {
    "source": "https://api.spacexdata.com/v5/launches/latest",
    "type": "dict",
    "description": "Raw data from the SpaceX API for the latest launch."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                   |
|-------------|---------|-----------------------------------------------|
| user_input  | Any     | Accepts orchestration triggers (unused in logic) |

### Output Topics

| Topic        | Type | Description                                            |
|--------------|------|------------------------------------------------------|
| launch_data  | dict | Dictionary with the latest SpaceX launch information  |


## License

Released under the MIT License.
