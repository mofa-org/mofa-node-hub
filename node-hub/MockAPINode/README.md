# MockAPINode

A Dora-rs node that fetches product data from a public mock JSON API and passes the result to downstream nodes. Designed for demonstration and prototyping with standardized API output.

## Features
- Simple demo node for API querying with Dora
- Serializes and sends API responses downstream
- Handles and reports API request errors

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
  - id: mock_api_node
    build: pip install -e .
    path: mock_api_node
    inputs:
      user_input: input/user_input  # Optional user input (can be placeholder)
    outputs:
      - api_response
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
  - id: your_custom_input
    build: pip install your-custom-node
    path: your_custom_input
    outputs:
      - user_input
  - id: mock_api_node
    build: pip install -e .
    path: mock_api_node
    inputs:
      user_input: your_custom_input/user_input
    outputs:
      - api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (typically string or dict)
* Metadata:

  ```json
  {
    "type": "any",
    "desc": "Trigger or parameter for the API call (optional)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type  | Description                                |
| ----------- | ----- | ------------------------------------------ |
| user_input  | any   | Trigger or input parameter for the API call |

### Output Topics

| Topic        | Type   | Description                           |
| ------------ | ------ | ------------------------------------- |
| api_response | object | API response payload (JSON-serializable) |


## License

Released under the MIT License.
