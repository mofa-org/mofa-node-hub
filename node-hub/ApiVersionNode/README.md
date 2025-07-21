# api_version_node

Query the public CEPiK Polish governmental transport API for its current version and emit the result as a structured message via MOFA/Dora-rs node interface.

## Features
- Simple access to the CEPiK version API
- Robust error handling with clear error messages
- Ready-to-integrate MofaAgent node for pipelines

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
  - id: api_version_node
    build: pip install -e .
    path: api_version_node
    inputs:
      user_input: input/user_input  # Placeholder, can be any value
    outputs:
      - api_version_response
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
  - id: my_input_source
    build: pip install -e my_input_source
    path: my_input_source
    outputs:
      - user_input

  - id: api_version_node
    build: pip install -e .
    path: api_version_node
    inputs:
      user_input: my_input_source/user_input
    outputs:
      - api_version_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (not used by this node, but required for interface compliance)
* Metadata:
  ```json
  {
    "description": "Stub user input, can be empty or any serializable value."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                 |
| ----------- | ------ | ------------------------------------------- |
| user_input  | any    | Placeholder input, not actually used        |

### Output Topics

| Topic                | Type          | Description                                    |
| -------------------- | ------------- | ---------------------------------------------- |
| api_version_response | dict / string | JSON API version response or error description |


## License

Released under the MIT License.
