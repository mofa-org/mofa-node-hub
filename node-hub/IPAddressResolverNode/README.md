# ip_address_node

A Dora-rs node to resolve public IP address and basic geo-details via external API. Returns your public IP and information (country, location, ISP), suitable as a service node or demo utility in chat chains.

## Features
- Lookup of current public IP address
- Returns detailed geo-info (location, country, ISP)
- Robust error handling for network/API issues

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
  - id: ip_resolver
    build: pip install -e ip_address_node
    path: ip_address_node
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
  - id: upstream
    build: pip install -e your-upstream-node
    path: your-upstream-node
    outputs:
      - user_input  # Message to trigger IP lookup

  - id: ip_resolver
    build: pip install -e ip_address_node
    path: ip_address_node
    inputs:
      user_input: upstream/user_input
    outputs:
      - ip_info
```

Your point source must output:

* Topic: `user_input`
* Data: any string or null (for chain triggering)
* Metadata:

  ```json
  {
    "description": "Unused: allows chaining in pipeline",
    "required": false,
    "type": "string or null"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type         | Description                           |
| ----------- | ------------ | ------------------------------------- |
| user_input  | string/null  | Placeholder; triggers IP API request. |

### Output Topics

| Topic    | Type   | Description                      |
| -------- | ------ | -------------------------------- |
| ip_info  | object | IP info from API or error string |


## License

Released under the MIT License.
