# coffee_api_node

Easy coffee data for your pipeline!

## Features
- Aggregates data from multiple public coffee APIs
- Returns structured and serializable outputs for downstream nodes
- Dora/Mofa-compliant message interface with parameter and output topics

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
  - id: coffee_api_node
    build: pip install -e .
    path: coffee_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - coffee_api_data
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
    path: my_input_node
    outputs:
      - user_input

  - id: coffee_api_node
    build: pip install -e .
    path: coffee_api_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - coffee_api_data
```

Your point source must output:

* Topic: `user_input`
* Data: Can be an empty string or placeholder (not used).
* Metadata:

  ```json
  {
    "description": "User or system input for triggering (can be empty)",
    "required": false
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ---------- | ------ | ----------------------------------------- |
| user_input | any    | Input to trigger API call (not utilized)  |

### Output Topics

| Topic            | Type   | Description                                         |
| ---------------- | ------ | ---------------------------------------------------|
| coffee_api_data  | dict   | Data from public coffee APIs mapped by endpoint URL |


## License

Released under the MIT License.
