# final_space_node

Fetch Final Space API Data via MofaAgent

## Features
- Fetches available Final Space API endpoints
- Retrieves all character entries and a specific character (ID=1)
- Robust error handling and JSON parsing

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
  - id: finalspace
    build: pip install -e .
    path: final_space_node
    inputs: {}
    outputs:
      - final_space_data
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
  - id: my_custom_node
    build: pip install -e ./my_custom_node
    path: my_custom_node
    outputs:
      - user_input
  - id: finalspace
    build: pip install -e .
    path: final_space_node
    inputs:
      user_input: my_custom_node/user_input
    outputs:
      - final_space_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable Python object (future-compatible; currently not required)
* Metadata:

  ```json
  {
    "description": "Input for FinalSpaceAPINode. Reserved for future use. May be any serializable object."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type           | Description                                       |
| ----------- | -------------- | ------------------------------------------------- |
| user_input  | Any            | Optional. Reserved for future compatibility.      |

### Output Topics

| Topic              | Type    | Description                                                |
| ------------------ | ------- | ---------------------------------------------------------- |
| final_space_data   | dict    | Dictionary with keys: 'data' (API responses) and 'errors'. |


## License

Released under the MIT License.
