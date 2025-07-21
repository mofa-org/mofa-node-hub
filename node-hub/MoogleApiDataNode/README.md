# moogle_api_node

Fetch Final Fantasy data from the MoogleAPI (games, monsters, characters) as a Dora node.

## Features
- Fetches data in real time from the public MoogleAPI (https://www.moogleapi.com/)
- Supports Dora pipeline integration via `receive_parameter`/`send_output`
- Robust error handling and response serialization

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
  - id: moogle_api_node
    build: pip install -e .
    path: moogle_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - moogle_api_data
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
  # Your custom upstream node
  - id: upstream_node
    build: pip install your-upstream
    path: your-upstream
    outputs:
      - user_input

  - id: moogle_api_node
    build: pip install -e .
    path: moogle_api_node
    inputs:
      user_input: upstream_node/user_input
    outputs:
      - moogle_api_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any valid parameter (can be a placeholder for this node)
* Metadata:

  ```json
  {
    "description": "User command or input to trigger a MoogleAPI fetch"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                           |
| -------------|--------|---------------------------------------|
| user_input    | any    | Placeholder input (triggers API call) |

### Output Topics

| Topic           | Type  | Description                                 |
| ----------------|-------|---------------------------------------------|
| moogle_api_data | dict  | Result data (games, monsters, characters)   |


## License

Released under the MIT License.
