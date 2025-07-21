# lucerne_visitor_node

A Dora-rs node that fetches real-time visitor frequency data for Lucerne using the alfons.io API. It handles secure API key management and robust error reporting, making it easy to integrate live visitor analytics into your own flows.

## Features
- Fetches real-time visitor sensor frequency data from alfons.io's public API for Lucerne
- Handles API key retrieval and error management securely
- Designed for easy orchestration within Dora/Mofa pipelines

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
  - id: lucerne_visitors
    build: pip install -e lucerne_visitor_node
    path: lucerne_visitor_node
    inputs:
      user_input: input/user_input
    outputs:
      - visitor_data
    env:
      API_KEY: your_api_key_here
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
  - id: my_input
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - user_input

  - id: lucerne_visitors
    build: pip install -e lucerne_visitor_node
    path: lucerne_visitor_node
    inputs:
      user_input: my_input/user_input
    outputs:
      - visitor_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable payload (even if not used by the node, include it for orchestration)
* Metadata:

  ```json
  {
    "description": "Trigger or pass payload to Lucerne visitor node. String or dict. May be empty."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                             |
| ---------- | ------ | --------------------------------------- |
| user_input | string | Orchestration trigger or input payload. |

### Output Topics

| Topic        | Type           | Description                                    |
| ------------ | --------------| ---------------------------------------------- |
| visitor_data | dict or string | Visitor frequency results or error information. |


## License

Released under the MIT License.
