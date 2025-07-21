# starwars_node

Star Wars Databank Dora Node: Unified Star Wars Universe API Aggregator

## Features
- Aggregates data from multiple Star Wars Databank API endpoints (locations, characters, droids)
- Handles failures and provides error diagnostics per endpoint
- Designed for seamless integration with Dora/Mofa agent-based workflows

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
  - id: starwars_db
    build: pip install -e .
    path: starwars_node
    inputs:
      user_input: null   # No required input, but topic provided for Dora compatibility
    outputs:
      - starwars_api_data
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
  - id: my_custom_node
    build: pip install <your-node>
    path: <your-node-path>
    inputs: {}
    outputs:
      - user_input

  - id: starwars_db
    build: pip install -e .
    path: starwars_node
    inputs:
      user_input: my_custom_node/user_input
    outputs:
      - starwars_api_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any payload (optional)
* Metadata:

  ```json
  { "description": "Optional user input as a trigger or data; can be null or omitted." }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                               |
| ----------- | ------- | -------------------------------------------------------- |
| user_input  | any     | Optional trigger or data payload to initiate API request |

### Output Topics

| Topic              | Type      | Description                                                         |
| ------------------ | --------- | ------------------------------------------------------------------- |
| starwars_api_data  | dict/json | Aggregated JSON data from API endpoints or error diagnostics object  |


## License

Released under the MIT License.
