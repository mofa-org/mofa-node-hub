# keyvalue_api_node

A Dora-rs node providing an interface to the Keyval.org API for simple remote key-value storage and retrieval.

## Features
- Sets a scientist value via the Keyval.org public key-value store
- Retrieves the scientist value from the store
- Returns aggregated status and response information through an output topic

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
  - id: keyvalue_api_node
    build: pip install -e .
    path: keyvalue_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - api_results
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
  - id: my_source_node
    build: pip install my_source_node
    path: my_source_node
    outputs:
      - user_input
  - id: keyvalue_api_node
    build: pip install -e .
    path: keyvalue_api_node
    inputs:
      user_input: my_source_node/user_input
    outputs:
      - api_results
```

Your point source must output:

* Topic: `user_input`
* Data: Any user-provided string (can be empty)
* Metadata:

  ```json
  {
    "description": "Optional user input for control or triggering."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| user_input  | string | Optional manual trigger or user data (unused) |

### Output Topics

| Topic        | Type   | Description                          |
| ------------ | ------ | ------------------------------------ |
| api_results  | dict   | Status codes, values, and responses  |


## License

Released under the MIT License.
