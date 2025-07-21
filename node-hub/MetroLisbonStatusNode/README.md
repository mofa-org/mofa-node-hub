# metro_lisbon_node

Get Lisbon Metro line statuses programmatically via Dora-rs node.

## Features
- Fetches real-time Lisbon Metro line status from the official endpoint
- Compatible with the MofaAgent/Dora node architecture
- Provides clear error reporting if the external API fails

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
  - id: metro_lisbon_status
    build: pip install -e metro_lisbon_node
    path: metro_lisbon_node
    inputs:
      user_input: input/user_input
    outputs:
      - lines_status
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
  - id: my_downstream_node
    build: pip install my-downstream-node
    path: my-downstream-node
    inputs:
      metro_status: metro_lisbon_status/lines_status
    outputs:
      - processed_status
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable prompt (required for future compatibility)
* Metadata:

  ```json
  {
    "description": "User input or trigger, passed through for framework compatibility"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                           |
| ----------- | ------ | ----------------------------------------------------- |
| user_input  | any    | Prompt or trigger parameter (future extensibility)    |

### Output Topics

| Topic         | Type           | Description                                 |
| ------------- | --------------| --------------------------------------------|
| lines_status  | dict/string    | Lisbon Metro status JSON or error message    |


## License

Released under the MIT License.
