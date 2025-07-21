# uspto_vehicle_node

A Dora-rs node for querying the USPTO IP Marketplace API for vehicle-related intellectual property listings. This node issues a synchronous search for patents concerning vehicles via the USPTO's REST API and outputs the results as JSON.

## Features
- Queries the USPTO IP Marketplace API for vehicle-related results
- Returns structured JSON data (or error messages) for downstream use
- Ready for composable Dora pipelines (input-agnostic)

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
  - id: uspto_vehicle_search
    build: pip install -e .
    path: uspto_vehicle_node
    inputs:
      user_input: input/user_input
    outputs:
      - uspto_vehicle_results
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
    build: pip install my-source-node
    path: my-source-node
    outputs:
      - user_input

  - id: uspto_vehicle_search
    build: pip install -e .
    path: uspto_vehicle_node
    inputs:
      user_input: my_input/user_input
    outputs:
      - uspto_vehicle_results

  - id: my_output
    build: pip install my-consumer-node
    path: my-consumer-node
    inputs:
      uspto_vehicle_results: uspto_vehicle_search/uspto_vehicle_results
```

Your point source must output:

* Topic: `user_input`
* Data: Anything (not used by this node)
* Metadata:

  ```json
  {
    "required": true,
    "type": "string",
    "description": "User input payload (ignored by node, required by interface)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                               |
| ----------- | ------ | --------------------------------------------------------- |
| user_input  | string | User input (ignored, required for interface compatibility) |

### Output Topics

| Topic                 | Type     | Description                                     |
| --------------------- | -------- | ----------------------------------------------- |
| uspto_vehicle_results | object   | USPTO vehicle search results (JSON or error msg) |

## License

Released under the MIT License.
