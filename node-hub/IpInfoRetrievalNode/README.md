# ip_info_node

Lightweight Dora-rs node to retrieve IP and domain information using [apip.cc](https://apip.cc) via HTTP requests. Aggregates responses from multiple API endpoints to provide structured IP and geolocation information.

## Features
- Retrieves information about specific IP addresses via API endpoints
- Supports domain-to-IP and metadata lookup (e.g., for vk.com)
- Returns public IP and corresponding currency/geolocation using a public API

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
  - id: ip_info_node
    build: pip install -e .
    path: ip_info_node
    inputs:
      user_input: input/user_input
    outputs:
      - ip_info_results
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
    build: pip install -e .
    path: your_point_source
    outputs:
      - user_input
  - id: ip_info_node
    build: pip install -e .
    path: ip_info_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - ip_info_results
```

Your point source must output:

* Topic: `user_input`
* Data: Ignored (can be `None` or empty)
* Metadata:

  ```json
  {
    "description": "Can be any value or omitted; ip_info_node does not expect payload data."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type      | Description                           |
| ----------- | --------- | ------------------------------------- |
| user_input  | Any/None  | Triggers IP info retrieval (optional) |

### Output Topics

| Topic           | Type    | Description                      |
| --------------- | ------- | -------------------------------- |
| ip_info_results | dict    | Aggregated API query responses   |

## License

Released under the MIT License.
