# iss_tracker_node

ISS Real-Time Location Microservice Node

## Features
- Retrieves the real-time location of the International Space Station (ISS)
- Outputs structured location data in a standard JSON format
- Handles and propagates API request errors clearly

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
  - id: iss_tracker
    build: pip install -e iss_tracker_node
    path: iss_tracker_node
    inputs:
      user_input: input/user_input  # Dummy/trigger input, not directly used
    outputs:
      - iss_location
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
  - id: iss_tracker
    build: pip install -e iss_tracker_node
    path: iss_tracker_node
    inputs:
      user_input: input/user_input  # Can be wired to a timer or a manual trigger
    outputs:
      - iss_location
```

Your point source must output:

* Topic: `points_to_track`
* Data: Flattened array of coordinates
* Metadata:

  ```json
  {
    "num_points": 0,
    "dtype": "float32",
    "shape": [0, 2]
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description               |
| ----------- | ------ | ------------------------ |
| user_input  | any    | Trigger for data refresh |

### Output Topics

| Topic        | Type   | Description                                     |
| ------------ | ------ | ----------------------------------------------- |
| iss_location | dict   | Real-time ISS location (API JSON or error info) |


## License

Released under the MIT License.
