# ip_vpn_proxy_checker

A Dora node for checking if a given IP address (default: 127.0.0.1) is flagged as a VPN or proxy using the baguette-radar.com API. Designed for use in automated pipelines or decision workflows, this node returns structured results or error information.

## Features
- Easy integration for IP risk assessment via API
- Handles and propagates all errors with clear output messages
- Designed for modular insertion into Dora and Mofa flows

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
  - id: ip_vpn_proxy_checker
    build: pip install -e ./ip_vpn_proxy_checker
    path: ip_vpn_proxy_checker
    inputs:
      user_input: input/user_input  # Optional placeholder for pipeline compatibility
    outputs:
      - vpn_proxy_check_result
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
  - id: your_upstream_node
    build: pip install -e ./your_upstream_node
    path: your_upstream_node
    outputs:
      - user_input

  - id: ip_vpn_proxy_checker
    build: pip install -e ./ip_vpn_proxy_checker
    path: ip_vpn_proxy_checker
    inputs:
      user_input: your_upstream_node/user_input
    outputs:
      - vpn_proxy_check_result
```

Your point source must output:

* Topic: `user_input`
* Data: any serializable data (not actually used in this node, placeholder for pipeline compatibility)
* Metadata:

  ```json
  {
    "dtype": "object",
    "description": "Arbitrary user parameter for input, accepted for interface compliance."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                      |
| ----------- | ------- | ------------------------------------------------ |
| user_input  | object  | Arbitrary input for pipeline compatibility only. |

### Output Topics

| Topic                 | Type   | Description                                                      |
| --------------------- | ------ | --------------------------------------------------------------- |
| vpn_proxy_check_result| object | Result dict from API, or error message if an exception occurred. |


## License

Released under the MIT License.
