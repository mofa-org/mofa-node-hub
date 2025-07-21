# financial_entity_node

A Dora-rs compatible node for retrieving real-time financial entity information (such as stock symbols) using external REST APIs. This node can be flexibly integrated with other nodes in your pipeline and supports dynamic user input.

## Features
- Fetches entity data for stock symbols from the Shodan entity database API
- Integrates seamlessly with Dora/MoFA dataflow pipelines
- Outputs results in standardized JSON (or plain text) for downstream nodes

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
  - id: financial_entity
    build: pip install -e .
    path: financial_entity_node
    inputs:
      user_input: input/user_input   # Optional, use for triggering requests
    outputs:
      - financial_data
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

  - id: financial_entity
    build: pip install -e .
    path: financial_entity_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - financial_data
```

Your point source must output:

* Topic: `user_input`
* Data: any value (ignored, used to trigger the call)
* Metadata:

  ```json
  {
    "description": "Trigger for financial data lookup. Can be any value."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                        |
|------------|--------|------------------------------------|
| user_input | any    | Triggers a fetch of financial data. |

### Output Topics

| Topic           | Type         | Description                              |
|-----------------|--------------|------------------------------------------|
| financial_data  | dict or str  | Financial entity data or error message.  |


## License

Released under the MIT License.
