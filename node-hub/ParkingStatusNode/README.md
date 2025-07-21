# parking_status_node

Real-time Zurich & Basel Parking Status Node

## Features
- Queries parking garage status from multiple Swiss cities via public API endpoints
- Configurable endpoints for flexible API selection
- Dora-rs compatible input/output to integrate with any pipeline

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
  - id: parking_status_node
    build: pip install -e .
    path: parking_status_node
    # No required inputs, but to comply can connect to tick or send dummy if needed
    inputs:
      user_input: dora/timer/millis/1000  # (Optional) triggers querying every second
    outputs:
      - parking_statuses
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
  - id: your_trigger_node
    build: pip install your-trigger-node
    path: your-trigger-node
    outputs:
      - user_input

  - id: parking_status_node
    build: pip install -e .
    path: parking_status_node
    inputs:
      user_input: your_trigger_node/user_input
    outputs:
      - parking_statuses
```

Your point source must output:

* Topic: `user_input`
* Data: any (can be dummy)
* Metadata:

  ```json
  {
    "description": "Any data to trigger the parking status query (can be an empty string or dict)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                       |
| ---------- | ------ | ------------------------------------------------- |
| user_input | any    | Input parameter to trigger a parking query        |

### Output Topics

| Topic            | Type      | Description                                                        |
| ---------------- | --------- | ------------------------------------------------------------------ |
| parking_statuses | list/dict | List of status dicts from endpoints, or error object if agent fails |


## License

Released under the MIT License.
