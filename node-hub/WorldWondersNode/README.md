# world_wonders_node

A Dora-rs node for fetching World Wonders data from the public World Wonders API, exposing both category and wonder information via structured output topics.

## Features
- Fetches wonder categories from the World Wonders public API
- Retrieves all world wonders details in structured JSON format
- Provides API error handling and serialization for robust workflows

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
  - id: world_wonders
    build: pip install -e .
    path: world_wonders_node
    inputs:
      user_input: input/user_input
    outputs:
      - categories
      - wonders
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
  - id: my_input_node
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - user_input

  - id: world_wonders
    build: pip install -e .
    path: world_wonders_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - categories
      - wonders
```

Your point source must output:

* Topic: `user_input`
* Data: String or object (used only for orchestration)
* Metadata:

  ```json
  {
    "description": "Orchestration signal input, can be any string or object. Required for agent step execution."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                     |
| ----------- | ------ | ----------------------------------------------- |
| user_input  | any    | Orchestration trigger to begin fetching process |

### Output Topics

| Topic      | Type   | Description                                         |
| ---------- | ------ | --------------------------------------------------- |
| categories | dict   | Categories from the World Wonders API, or error info |
| wonders    | dict   | Wonder details from the API, or error info           |


## License

Released under the MIT License.
