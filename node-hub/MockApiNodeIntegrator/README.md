# mock_api_node

A Dora-rs node for querying mock e-commerce REST API endpoints (products, coupons, carts, users) and forwarding the results to your pipeline. This node enables integration with demo or testing APIs by selecting endpoints via upstream messages.

## Features
- Simple access to mock e-commerce API endpoints
- Dynamic endpoint selection through message passing
- Robust error handling with descriptive output

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
  - id: mock_api
    build: pip install -e mock_api_node
    path: mock_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - api_result
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
  - id: input_node
    build: pip install your-input-node  # Your node sending endpoint keywords
    path: your-input-node
    outputs:
      - user_input

  - id: mock_api
    build: pip install -e mock_api_node
    path: mock_api_node
    inputs:
      user_input: input_node/user_input
    outputs:
      - api_result
```

Your point source must output:

* Topic: `user_input`
* Data: Endpoint key as a string, e.g., "products", "coupons", "carts", or "users"
* Metadata:

  ```json
  {
    "type": "str",
    "description": "Key indicating the mock API endpoint (products, coupons, carts, users)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type | Description                            |
|-------------|------|----------------------------------------|
| user_input  | str  | Key indicating the mock API endpoint    |

### Output Topics

| Topic      | Type    | Description                                              |
|------------|---------|---------------------------------------------------------|
| api_result | object  | API JSON response or error message dict                  |

## License

Released under the MIT License.
