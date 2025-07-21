# football_data_api_node

Fetch live and up-to-date football competitions data from the Football Data API (football-data.org) with a simple Dora-rs compatible node. Designed for integration into ML pipelines, dashboards, or intelligent agents using the Dora ecosystem or the Mofa agent framework.

## Features
- Retrieves a full list of football competitions from the Football Data API
- Simple, stateless node design for Dora-rs or Mofa workflows
- Robust error handling and diagnostics via output topic

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
  - id: api_node
    build: pip install -e football_data_api_node
    path: football_data_api_node
    env:
      FOOTBALL_DATA_API_KEY: <your_api_key_here>
    inputs:
      user_input: input/user_input
    outputs:
      - competitions_data
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
  - id: api_node
    build: pip install -e football_data_api_node
    path: football_data_api_node
    env:
      FOOTBALL_DATA_API_KEY: <your_api_key_here>
    inputs:
      user_input: your_input_node/your_parameter
    outputs:
      - competitions_data

  - id: downstream
    build: <your-build-spec>
    path: <your-node-path>
    inputs:
      competitions_data: api_node/competitions_data
```

Your point source must output:

* Topic: `user_input`
* Data: String (can be any value, it's ignored)
* Metadata:

  ```json
  {
    "description": "Any string. Value is ignored by this node. Required for pipeline compliance."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                                          |
| ----------- | ------ | -------------------------------------------------------------------- |
| user_input  | str    | Input string, ignored by this node (for compliance only)             |

### Output Topics

| Topic              | Type         | Description                               |
| ------------------ | ------------ | ----------------------------------------- |
| competitions_data  | dict or str  | Football competitions data or error info  |

## License

Released under the MIT License.
