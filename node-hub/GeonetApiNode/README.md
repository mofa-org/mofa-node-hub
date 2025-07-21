# geonet_api_node

Query global DNS and ping results using Shodan's GeoNet API.

## Features
- DNS lookup from multiple geographic locations
- Ping results from various countries using the GeoNet API
- Seamless integration with Dora-rs workflows and messaging

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: geonet
    build: pip install -e geonet_api_node
    path: geonet_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - dns_lookup_result
      - ping_result
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
  - id: my_input
    build: pip install my-input-node
    path: my-input
    outputs:
      - user_input

  - id: geonet
    build: pip install -e geonet_api_node
    path: geonet_api_node
    inputs:
      user_input: my_input/user_input
    outputs:
      - dns_lookup_result
      - ping_result
```

Your point source must output:

* Topic: `user_input`
* Data: String (dummy or can be used for future extensibility)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Dummy input for workflow compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                       |
| ----------- | ------ | --------------------------------- |
| user_input  | string | Dummy input for workflow trigger. |

### Output Topics

| Topic              | Type           | Description                    |
| ------------------ | --------------| ------------------------------ |
| dns_lookup_result  | JSON/dict/text | DNS lookup result or error.    |
| ping_result        | JSON/dict/text | Ping result or error.          |


## License

Released under the MIT License.
