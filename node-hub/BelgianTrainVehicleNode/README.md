# belgian_train_vehicle

Real-time retrieval of Belgian train vehicle data from iRail API for Dora-rs pipelines.

## Features
- Fetches real-time status and composition information for Belgian trains via the iRail API
- Simple integration: receives dummy input to enable graph-based flows and outputs API results
- Robust error handling: outputs structured errors for integration into ML ops pipelines

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
  - id: belgian_train_vehicle
    build: pip install -e .
    path: belgian_train_vehicle
    inputs:
      user_input: input/user_input
    outputs:
      - vehicle_data
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
  - id: my_upstream_node
    build: pip install -e my_upstream_node
    path: my_upstream_node
    outputs:
      - user_input
  - id: belgian_train_vehicle
    build: pip install -e .
    path: belgian_train_vehicle
    inputs:
      user_input: my_upstream_node/user_input
    outputs:
      - vehicle_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy, not used)
* Metadata:

  ```json
  {"type": "any", "description": "Not used. Pass any value to trigger vehicle request"}
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                       |
| ----------| ------ | ------------------------------------------------- |
| user_input | any    | Dummy input to trigger vehicle data fetch         |

### Output Topics

| Topic        | Type   | Description                                          |
| ------------| ------ | ---------------------------------------------------- |
| vehicle_data | dict   | iRail API vehicle result or error response           |

## License

Released under the MIT License.
