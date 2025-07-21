# ip_geolocation_greeter

A Dora-rs node that returns a localized greeting for a given IP address by querying the [HelloSalut API](https://www.hellosalut.com/). Receives an IP address as input and outputs a greeting based on the geolocation.

## Features
- Retrieve greetings localized to the country of the IP address
- Handles invalid or missing IP addresses gracefully
- Standard Dora parameter and output interface

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
  - id: ip_greeting
    build: pip install -e .
    path: ip_geolocation_greeter
    inputs:
      ip: input/ip
    outputs:
      - greeting_response
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
    build: pip install my-ip-source
    path: my_ip_source
    outputs:
      - ip

  - id: ip_greeting
    build: pip install -e .
    path: ip_geolocation_greeter
    inputs:
      ip: my_ip_source/ip
    outputs:
      - greeting_response
```

Your point source must output:

* Topic: `ip`
* Data: String with the IP address
* Metadata:

  ```json
  {
    "type": "string",
    "description": "IPv4 or IPv6 address to localize greeting"
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                       |
|-------|--------|-----------------------------------|
| ip    | string | IP address to lookup (IPv4/IPv6)  |

### Output Topics

| Topic             | Type   | Description                                        |
|-------------------|--------|----------------------------------------------------|
| greeting_response | object | Localized greeting and geolocation result or error |

## License

Released under the MIT License.
