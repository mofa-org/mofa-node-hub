# ip_geolocation_node

IP address geolocation Dora-rs node for dynamic location lookup via the IP2Location public API.

## Features
- Real-time IP geolocation lookup using IP2Location public API
- Simple parameter interface (input: `ip`, output: complete geolocation result)
- Robust error handling and reporting with standardized error messages

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
  - id: geolocation
    build: pip install -e ip_geolocation_node
    path: ip_geolocation_node
    inputs:
      ip: input/ip
    outputs:
      - geolocation_result
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
  - id: my_ip_source
    build: pip install -e my-ip-source
    path: my-ip-source
    outputs:
      - ip  # should be a string containing the IP address

  - id: geolocation
    build: pip install -e ip_geolocation_node
    path: ip_geolocation_node
    inputs:
      ip: my_ip_source/ip
    outputs:
      - geolocation_result
```

Your point source must output:

* Topic: `ip`
* Data: A non-empty string containing the IP address to lookup
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "IPv4 or IPv6 address as a string"
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                |
|-------|--------|----------------------------|
| ip    | string | IP address to lookup (IPv4 or IPv6 as a string) |

### Output Topics

| Topic              | Type   | Description              |
|--------------------|--------|--------------------------|
| geolocation_result | dict   | Geolocation result object or error report |

## License

Released under the MIT License.
