# openfda_food_enforcement

Query FDA Food Enforcement Reports with a Dora-rs Node

## Features
- Fetches the latest 10 food enforcement reports from the openFDA public API
- Sends results directly as output in a Dora-compatible format
- Handles network errors with meaningful error outputs

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
  - id: openfda_food
    build: pip install -e .
    path: openfda_food_enforcement
    inputs:
      user_input: input/user_input  # dummy input, can come from any node
    outputs:
      - food_enforcement_data
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
  - id: user_control
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input
  - id: openfda_food
    build: pip install -e .
    path: openfda_food_enforcement
    inputs:
      user_input: user_control/user_input
    outputs:
      - food_enforcement_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any dummy data (this node ignores the contents)
* Metadata:

  ```json
  {
    "description": "dummy user input, not used but required for protocol"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                        |
|-----------|--------|------------------------------------|
| user_input | any    | Dummy input (not used by the node)  |

### Output Topics

| Topic                  | Type | Description                                 |
|------------------------|------|---------------------------------------------|
| food_enforcement_data  | dict | FDA food enforcement data or error message  |


## License

Released under the MIT License.
