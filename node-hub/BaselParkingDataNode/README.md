# basel_parking_node

BaselParkingDataNode: Dora-rs node for fetching open Basel parking lot data

## Features
- Retrieves real-time parking lot data for Basel from the official open data endpoint
- Robust error handling with serializable outputs
- Compatible with MOFA orchestrator parameter passing and Dora-rs pipeline integration

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
  - id: parking
    build: pip install -e basel_parking_node
    path: basel_parking_node
    inputs:
      user_input: input/user_input
    outputs:
      - parking_data
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
    build: pip install your-node  # Replace as needed
    path: your-node-path
    outputs:
      - user_input

  - id: parking
    build: pip install -e basel_parking_node
    path: basel_parking_node
    inputs:
      user_input: my_input/user_input
    outputs:
      - parking_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable (can be null or string)
* Metadata:

  ```json
  {
    "description": "Trigger input, not required by parking node but enables orchestrator pipeline compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type     | Description                                        |
| ---------- | -------- | -------------------------------------------------- |
| user_input | Any      | Optional parameter for pipeline compatibility      |

### Output Topics

| Topic         | Type   | Description                                             |
| ------------- | ------ | ------------------------------------------------------ |
| parking_data  | Dict   | Parking records data OR error dict if fetch fails       |


## License

Released under the MIT License.
