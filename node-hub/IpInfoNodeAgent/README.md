# ip_info_node

Get your internet IP and geolocation in Dora-rs pipelines.

## Features
- Queries the public IP and geolocation using ipinfo.io
- Seamless integration with Dora-rs graphs and messaging
- Graceful error handling—always returns output, even on failure

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
  - id: ip_info
    build: pip install -e .
    path: ip_info_node
    inputs:
      user_input: input/user_input  # Optional; can be connected to another node or left empty
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
  - id: my_input_node
    build: pip install your-input-node
    path: my_input_node
    outputs:
      - user_input

  - id: ip_info
    build: pip install -e .
    path: ip_info_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - ip_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (optional, e.g., a trigger or command)
* Metadata:

  ```json
  {
    "dtype": "string",
    "optional": true
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                |
| ---------- | ------ | ------------------------- |
| user_input | string | Optional user input value |

### Output Topics

| Topic    | Type   | Description                                                 |
| -------- | ------ | ----------------------------------------------------------- |
| ip_info  | dict   | IP and geolocation as returned from ipinfo.io (or error)    |


## License

Released under the MIT License.
