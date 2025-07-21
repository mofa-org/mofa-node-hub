# materia_fusion_node

A Dora-rs node for interacting with a Crisis Core Materia Fusion API. This node supports listing all materia, checking backend health, and fusing two materia via a simple input interface, leveraging Dora message passing and HTTP requests.

## Features
- List all available materia via remote API
- Health check for the remote fusion backend
- Fuse two materia with provided parameters

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
  - id: materia_fusion
    build: pip install -e .
    path: materia_fusion_node
    inputs:
      action: input/action
      payload: input/payload
    outputs:
      - materia_list
      - health_status
      - fusion_result
      - invalid_action
      - error
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
  - id: custom_input
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - action
      - payload
  - id: materia_fusion
    build: pip install -e .
    path: materia_fusion_node
    inputs:
      action: custom_input/action
      payload: custom_input/payload
    outputs:
      - materia_list
      - health_status
      - fusion_result
      - invalid_action
      - error
```

Your point source must output:

* Topic: `action` and `payload`
* Data: For `action`, one of `list`, `health`, or `fuse` (string). For `payload`, a JSON string if `action = 'fuse'`.
* Metadata:

  ```json
  {
    "action": "list | health | fuse",
    "payload": "{\"materia_a\":..., \"materia_b\":...}" // only for action=fuse
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                       |
| -------------| -------| --------------------------------- |
| action       | str    | Action to perform: list, health, or fuse |
| payload      | str    | JSON string containing fusion payload, required if action=fuse |

### Output Topics

| Topic          | Type    | Description                    |
| -------------- | ------- | ------------------------------ |
| materia_list   | object  | JSON result of all materia     |
| health_status  | object  | JSON health check or status    |
| fusion_result  | object  | Result of fusion attempt       |
| invalid_action | object  | Error if action value unknown  |
| error          | object  | Any fatal error encountered    |


## License

Released under the MIT License.
