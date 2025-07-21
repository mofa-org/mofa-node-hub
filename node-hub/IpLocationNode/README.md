# ip_location_node

IP Geolocation Query Node for Dora/Mofa Pipelines

## Features
- Fetches geolocation data for multiple hard-coded IP addresses via web API
- Outputs standardized and serializable JSON results (with error handling)
- Designed for seamless integration as a node in Dora/Mofa pipelines (supports dataflow from upstream nodes)

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
  - id: ip_locator
    build: pip install -e ip_location_node
    path: ip_location_node
    inputs:
      user_input: upstream_node/some_output  # Optional for dataflow, can be left unconnected
    outputs:
      - ip_location_results
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
  - id: my_preprocess
    build: pip install -e my_preprocess
    path: my_preprocess
    outputs:
      - user_input

  - id: ip_locator
    build: pip install -e ip_location_node
    path: ip_location_node
    inputs:
      user_input: my_preprocess/user_input
    outputs:
      - ip_location_results
```

Your point source must output:

* Topic: `user_input`
* Data: Any (unused, pass-through for chaining)
* Metadata:

  ```json
  {
    "description": "Any data passed through for pipeline continuity; not used in this node."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                   |
| ----------- | ------- | --------------------------------------------- |
| user_input  | Any     | Optional data for chaining nodes in pipeline. |

### Output Topics

| Topic               | Type           | Description                                               |
| ------------------- | -------------- | --------------------------------------------------------- |
| ip_location_results | List[dict]     | List of geolocation results or errors for each IP address |

## License

Released under the MIT License.
