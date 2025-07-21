# nyc_service_node

Query NYC Open Data Service Requests (Dora Node)

## Features
- Queries the NYC 311 Service Requests API to fetch recent service requests
- Handles HTTP/network and JSON errors with clear error outputs
- Truncates large outputs for easy downstream processing

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
  - id: nyc_service_node
    build: pip install -e .
    path: nyc_service_node
    inputs:
      user_input: input/user_input  # (Unused, for compatibility)
    outputs:
      - service_requests
      - error
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
  - id: my_input_node
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input

  - id: nyc_service_node
    build: pip install -e .
    path: nyc_service_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - service_requests
      - error

  - id: my_output_node
    build: pip install my-output-node
    path: my-output-node
    inputs:
      service_requests: nyc_service_node/service_requests
      error: nyc_service_node/error
```

Your point source must output:

* Topic: `user_input`
* Data: (any, ignored)
* Metadata:

  ```json
  {
    "description": "Parameter placeholder; content ignored by nyc_service_node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                         |
| ---------- | ------ | ----------------------------------- |
| user_input | any    | Parameter placeholder; not required. |

### Output Topics

| Topic            | Type   | Description                                                          |
| ---------------- | ------ | -------------------------------------------------------------------- |
| service_requests | list   | List (max 100) of NYC 311 service request records as JSON dictionaries|
| error            | str    | Error messages for HTTP or JSON parsing issues                       |


## License

Released under the MIT License.
