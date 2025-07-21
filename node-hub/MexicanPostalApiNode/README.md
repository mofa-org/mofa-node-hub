# mexican_postal_node

Fetch Mexican Postal Code Information via Remote API

## Features
- Query postal code data from public REST endpoints
- Aggregates results from multiple endpoints in one call
- Structured error reporting included in output

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
  - id: postal_info_node
    build: pip install -e .
    path: mexican_postal_node
    inputs:
      user_input: input/user_input  # Placeholder for dataflow compatibility
    outputs:
      - postal_info_results
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
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input

  - id: postal_info_node
    build: pip install -e .
    path: mexican_postal_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - postal_info_results
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (used only for compatibility)
* Metadata:

  ```json
  {
    "description": "Any field, ignored by this node. For dataflow wiring only."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                                                  |
| ------------|----------|-------------------------------------------------------------|
| user_input  | Any      | Placeholder input; not used for queries, required by system. |

### Output Topics

| Topic               | Type    | Description                                        |
|---------------------|---------|----------------------------------------------------|
| postal_info_results | Object  | Array of postal info results with errors if any    |

## License

Released under the MIT License.
