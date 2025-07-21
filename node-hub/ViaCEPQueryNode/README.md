# viacep_query_node

A Dora-rs node for querying the Brazilian ViaCEP API to fetch address details for a specified postal code (CEP).

## Features
- Fetches address information from the ViaCEP API
- Simple integration as an agent node in Dora-rs pipelines
- Returns results as structured JSON output

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
  - id: viacep_query_node
    build: pip install -e .
    path: viacep_query_node
    inputs:
      user_input: input/form/user_input  # provide a user input parameter if required
    outputs:
      - viacep_response
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
    build: pip install your-point-source-node
    path: your-point-source-node
    outputs:
      - user_input

  - id: viacep_query_node
    build: pip install -e .
    path: viacep_query_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - viacep_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any (can be an empty string, as no input is used in this example)
* Metadata:

  ```json
  {
    "format": "string",
    "description": "User input parameter (may be unused)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                        |
| ---------- | ------ | ---------------------------------- |
| user_input | string | User parameter (not used directly) |

### Output Topics

| Topic           | Type | Description                                      |
| --------------- | ---- | ------------------------------------------------ |
| viacep_response | JSON | The address result from ViaCEP API, or error msg |


## License

Released under the MIT License.
