# address_lookup_node

Hong Kong Address Lookup Dora Node

## Features
- Query Hong Kong government address lookup API
- Robust automatic error handling and retries
- Easy integration with Dora pipeline for address search

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
  - id: address_lookup
    build: pip install -e .
    path: address_lookup_node
    inputs:
      q: input/q
    outputs:
      - address_lookup_result
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
  - id: your_input_source
    build: pip install your-node  # Replace with your node's name
    path: your-node-path         # Replace with your node's path
    outputs:
      - q

  - id: address_lookup
    build: pip install -e .
    path: address_lookup_node
    inputs:
      q: your_input_source/q
    outputs:
      - address_lookup_result
```

Your point source must output:

* Topic: `q`
* Data: String with address query
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Address query string for lookup"
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                 |
|-------|--------|-----------------------------|
| q     | string | Address query string input  |

### Output Topics

| Topic                 | Type  | Description                                 |
|-----------------------|-------|---------------------------------------------|
| address_lookup_result | JSON  | Address lookup API response or error result |


## License

Released under the MIT License.
