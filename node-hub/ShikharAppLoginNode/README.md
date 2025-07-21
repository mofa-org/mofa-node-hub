# shikhar_login_node

Agent for Shikhar App Login Endpoint

## Features
- Provides access to the Shikhar app login endpoint via HTTP GET
- Includes robust error handling and retry logic
- Easily extendable to accept input parameters for future expansion

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
  - id: shikhar_login_node
    build: pip install -e .
    path: shikhar_login_node
    inputs:
      user_input: input/user_input
    outputs:
      - shikhar_login_response
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
  - id: user_input_node
    build: pip install your-input-node
    path: user-input-node
    outputs:
      - user_input
  - id: shikhar_login_node
    build: pip install -e .
    path: shikhar_login_node
    inputs:
      user_input: user_input_node/user_input
    outputs:
      - shikhar_login_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (for future extensibility; currently unused)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "User input for Shikhar app login endpoint (currently optional and unused)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                                                |
| ----------| ------ | ------------------------------------------------------------------------------------------ |
| user_input | string | Optional future input for Shikhar login (not currently used, reserved for future versions) |

### Output Topics

| Topic                   | Type   | Description                                                    |
| ----------------------- | ------ | -------------------------------------------------------------- |
| shikhar_login_response  | string | Returns raw response from Shikhar login endpoint or error JSON  |

## License

Released under the MIT License.
