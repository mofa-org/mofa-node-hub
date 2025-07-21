# ip_country_node

A Dora-rs node that retrieves the current machine's public IP address and associated country information using the https://api.miip.my API, designed for integration and compatibility with MOFA agent-based workflows.

## Features
- Retrieves public IP address and corresponding country info
- Designed for easy dataflow integration (dummy input supported)
- Structured, serializable output for downstream nodes

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
  - id: ip_lookup
    path: ip_country_node
    build: pip install -e ip_country_node
    inputs:
      user_input: input/user_input
    outputs:
      - ip_country_info
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
    path: your_point_source_node
    build: pip install -e your_point_source_node
    outputs:
      - user_input

  - id: ip_lookup
    path: ip_country_node
    build: pip install -e ip_country_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - ip_country_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (dummy placeholder accepted)
* Metadata:

  ```json
  {
    "description": "Any value; used to facilitate graph connectivity."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                                 |
| ----------- | -------- | ------------------------------------------- |
| user_input  | Any      | Dummy input to enable dataflow connections. |

### Output Topics

| Topic            | Type   | Description                                                   |
| ---------------- | ------ | ------------------------------------------------------------- |
| ip_country_info  | dict   | The result from api.miip.my, e.g., public IP and country info |

## License

Released under the MIT License.
