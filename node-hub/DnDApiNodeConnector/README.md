# dnd_api_node

DnDApiNodeConnector: Dora node for querying Dungeons & Dragons 5e API endpoints and returning data as structured responses.

## Features
- Query D&D 5e API for features, monsters, or classes
- Parameter-driven endpoint selection (operation)
- Returns JSON data or error diagnostics on output

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
  - id: dnd_api_node
    build: pip install -e .
    path: dnd_api_node
    inputs:
      user_input: input/user_input
      operation: input/operation
    outputs:
      - api_response
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
  - id: my_input
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input
      - operation

  - id: dnd_api_node
    build: pip install -e .
    path: dnd_api_node
    inputs:
      user_input: my_input/user_input
      operation: my_input/operation
    outputs:
      - api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any meaningful input or dummy value (can be ignored)
* Metadata:

  ```json
  {
    "description": "Parameter input for the node, can be a dummy value. Required for triggering.",
    "required": true,
    "type": "Any or String"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                    |
| -------------| ------ | ---------------------------------------------- |
| user_input    | Any    | Required trigger/data for flow, can be ignored |
| operation     | String | Operation code for endpoint (features/monster/classes) |

### Output Topics

| Topic        | Type   | Description                                   |
| ------------ | ------ | --------------------------------------------- |
| api_response | Dict   | API response from D&D 5e API, or error info   |


## License

Released under the MIT License.
