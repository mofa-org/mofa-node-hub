# WaybackMachineNode

Archive.org Wayback Snapshot Query Node for Dora

## Features
- Fetches the latest Wayback Machine snapshot for a given URL (hardcoded to apple.com)
- Dora-compatible node that sends HTTP query results as outputs
- Robust error handling with JSON error messages

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: wayback_machine
    build: pip install -e wayback_machine_node
    path: wayback_machine_node
    inputs:
      user_input: input/user_input
    outputs:
      - wayback_snapshot
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
    path: my-input-node
    outputs:
      - user_input

  - id: wayback_machine
    build: pip install -e wayback_machine_node
    path: wayback_machine_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - wayback_snapshot
```

Your point source must output:

* Topic: `user_input`
* Data: Any (not used in this node, but required for interface)
* Metadata:

  ```json
  {
    "description": "Any payload for input. This node does not use or inspect the value, but it must be provided to match the API."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description        |
| ----------- | ------ | ------------------ |
| user_input  | any    | Triggers a Wayback snapshot fetch. (Payload ignored) |

### Output Topics

| Topic             | Type   | Description                                |
| ----------------- | ------ | ------------------------------------------ |
| wayback_snapshot  | dict   | JSON response from the Wayback Machine API |


## License

Released under the MIT License.
