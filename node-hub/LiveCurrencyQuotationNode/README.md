# currency_quotation_node

Live currency quotation retrieval node for Dora-rs pipelines

## Features
- Sends real-time currency quotations from a live API endpoint
- Simple integration as an agent node with Dora/Mofa agent interface
- Robust error handling and JSON serialization of API results

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
  - id: currency_quotation
    build: pip install -e .
    path: currency_quotation_node
    inputs:
      user_input: input/user_input   # Dummy input to enable agent communication
    outputs:
      - currency_quotation
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
  - id: your_input_node
    build: pip install -e your_input_node
    path: your_input_node
    outputs:
      - user_input

  - id: currency_quotation
    build: pip install -e .
    path: currency_quotation_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - currency_quotation
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy data, e.g. None or placeholder)
* Metadata:

  ```json
  {
    "dtype": "object",
    "desc": "Dummy trigger object for currency query"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                   |
| ----------- | ------- | --------------------------------------------- |
| user_input  | object  | Dummy input to allow triggering the agent run |

### Output Topics

| Topic               | Type   | Description                                    |
| ------------------- | ------ | ---------------------------------------------- |
| currency_quotation  | dict   | Live currency quotation or error information   |

## License

Released under the MIT License.
