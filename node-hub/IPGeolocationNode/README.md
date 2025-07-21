# ip_geolocation_node

Query IP Geolocation data from a public API via a reproducible Dora-rs node.

## Features
- Query geolocation info for a given IP address (example endpoint used)
- Expose country and other metadata data via Dora output
- Safe error reporting through structured message output

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
  - id: ip_geolocator
    build: pip install -e .
    path: ip_geolocation_node
    inputs:
      user_input: input/user_input
    outputs:
      - geolocation_info
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
  - id: ip_point_source
    build: pip install your-point-source
    path: point_source_node
    outputs:
      - user_input
  - id: ip_geolocator
    build: pip install -e .
    path: ip_geolocation_node
    inputs:
      user_input: ip_point_source/user_input
    outputs:
      - geolocation_info
```

Your point source must output:

* Topic: `user_input`
* Data: string representing raw input or a dummy string (API uses a fixed IP for this demo)
* Metadata:

  ```json
  {
    "dtype": "string"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                       |
| ----------|--------|--------------------------------------------------|
| user_input | string | Dummy input. Unused; placeholder for node API.    |

### Output Topics

| Topic            | Type             | Description                          |
| ---------------- | ---------------- | ------------------------------------ |
| geolocation_info | dict or JSON obj | Geolocation info from country.is API |

## License

Released under the MIT License.
