# multifon_balance_node

Multifon Client Balance Node for Dora-rs

A Dora-rs node for securely querying Multifon client balance via Megafon's official API. Credentials are loaded from environment variables, and results are relayed with standardized error handling.

## Features
- Queries client balance from Multifon API
- Secure credential and error management
- Easy integration with MofaAgent and Dora pipelines

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
  - id: multifon_balance
    build: pip install -e .
    path: multifon_balance_node.py
    env:
      MULTIFON_LOGIN: ${MULTIFON_LOGIN}
      MULTIFON_PASSWORD: ${MULTIFON_PASSWORD}
    inputs:
      user_input: upstream/user_input
    outputs:
      - balance_result
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
  - id: upstream
    build: pip install -e .
    path: upstream_node.py
    outputs:
      - user_input
  - id: multifon_balance
    build: pip install -e .
    path: multifon_balance_node.py
    inputs:
      user_input: upstream/user_input
    outputs:
      - balance_result
```

Your point source must output:

* Topic: `user_input`
* Data: User input parameter (string or dict)
* Metadata:

  ```json
  {
    "type": "string",
    "required": true,
    "description": "Input data to initiate balance check."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                 |
| ----------- | ------ | -------------------------- |
| user_input  | any    | Input data to trigger balance check |

### Output Topics

| Topic           | Type   | Description                         |
| -------------- | ------ | ----------------------------------- |
| balance_result | dict   | Result dict with 'status_code', 'data', and error info |


## License

Released under the MIT License.
