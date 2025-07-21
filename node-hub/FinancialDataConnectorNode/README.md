# financial_data_node

Simple Financial Data API Connector Node

## Features
- Connects to financialdata.net open API endpoint
- Fetches and returns API response (JSON or text)
- Graceful error handling and serializable error output

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
  - id: finance_connector
    build: pip install -e financial_data_node
    path: financial_data_node
    inputs:
      user_input: input/user_input  # Dummy input for integration
    outputs:
      - financial_data_response
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
  - id: your_node
    build: pip install your-node
    path: your_node
    outputs:
      - user_input

  - id: finance_connector
    build: pip install -e financial_data_node
    path: financial_data_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - financial_data_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable dummy value (e.g., string or dict)
* Metadata:

  ```json
  {"type": "string", "description": "Dummy trigger input for financial data node."}
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                 |
| ----------| ------ | ------------------------------------------- |
| user_input | any    | Dummy trigger input for running the node    |

### Output Topics

| Topic                   | Type    | Description                                                            |
| ----------------------- | ------- | ---------------------------------------------------------------------- |
| financial_data_response | object  | API response from https://financialdata.net/documentation or error msg |

## License

Released under the MIT License.
