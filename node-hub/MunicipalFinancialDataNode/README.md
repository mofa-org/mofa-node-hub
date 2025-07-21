# municipal_financial_node

Access South African municipal financial data cubes via Dora-rs node.

## Features
- Fetches general municipal data cubes from Treasury API
- Retrieves the repairs and maintenance financial model
- Integrates easily into Dora-rs pipelines with structured outputs

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
  - id: municipal_financial_node
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input  # Dummy; not required for data fetch
    outputs:
      - municipal_financial_data
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
    build: ... # e.g., pip install your-custom-node
    path: ...  # path to your custom node
    outputs:
      - user_input

  - id: municipal_financial_node
    build: pip install -e .
    path: .
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - municipal_financial_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (dummy, will be ignored)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Unused. Placeholder for compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description   |
| ----------- | ------ | ------------- |
| user_input  | any    | Placeholder; not consumed by the node |

### Output Topics

| Topic                    | Type   | Description                                                    |
| ------------------------ | ------ | -------------------------------------------------------------- |
| municipal_financial_data | dict   | Contains data cubes and repairs/maintenance model, or error msg |


## License

Released under the MIT License.
