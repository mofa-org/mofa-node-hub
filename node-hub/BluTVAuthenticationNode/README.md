# blutv_auth_node

A Dora-rs node for programmatic access to the BluTV login page, exposing it as an HTTP response stream for use in agent-based workflows and node pipelines.

## Features
- Automated retrieval of BluTV login page using HTTP GET
- Dora-rs agent compatibility, including dynamic parameter passing
- Simplified output handling as a Dora-compatible output topic

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
  - id: blutv_auth
    build: pip install -e blutv_auth_node
    path: blutv_auth_node
    inputs:
      user_input: input/user_input
    outputs:
      - auth_response
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
  - id: point_source
    build: pip install your-point-source-node  # Replace with your node's name
    path: your-point-source-node               # Replace with your node's path
    outputs:
      - user_input
  - id: blutv_auth
    build: pip install -e blutv_auth_node
    path: blutv_auth_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - auth_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any dummy input (empty string or placeholder)
* Metadata:

  ```json
  {
    "description": "Dummy input to trigger BluTV authentication request"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                 |
| ----------- | ------ | ------------------------------------------- |
| user_input  | any    | Dummy trigger; initiates authentication GET |

### Output Topics

| Topic         | Type   | Description                            |
| ------------- | ------ | -------------------------------------- |
| auth_response | string | BluTV login page as raw text or error  |

## License

Released under the MIT License.
