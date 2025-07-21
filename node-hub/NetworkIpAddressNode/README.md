# network_ip_node

Query your external IPv4 address programmatically via an HTTP request, ready for Dora-rs node pipelines.

## Features
- Fetches the host's public IPv4 address using the ipty.org service
- Accepts parameterized input from other nodes or user requests
- Compatible with Dora-rs and MOFA agent pipelines

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
  - id: network_ip_node
    build: pip install -e .
    path: network_ip_node
    inputs:
      user_input: input/user_input
    outputs:
      - ip_info
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
  - id: your_point_source
    build: pip install -e your_point_source
    path: your_point_source
    outputs:
      - user_input

  - id: network_ip_node
    build: pip install -e .
    path: network_ip_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - ip_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or dictionary
* Metadata:

  ```json
  {
    "type": "string | dict",
    "description": "Input parameter to trigger IP lookup"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type             | Description                         |
| ----------| ---------------- | ----------------------------------- |
| user_input| string or dict   | Input trigger or hint (not required) |

### Output Topics

| Topic    | Type         | Description                              |
| -------- | ------------ | ---------------------------------------- |
| ip_info  | dict         | {'ip' (str)} on success or {'error': str} on failure |


## License

Released under the MIT License.
