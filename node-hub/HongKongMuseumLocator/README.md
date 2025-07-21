# hk_museum_locator

Easily retrieve museum locations in Hong Kong using a Dora-rs compatible node that fetches and outputs data from the Hong Kong GeoData API.

## Features
- Fetches up-to-date locations of museums in Hong Kong
- Integrates with node chains with standardized input/output parameters
- Handles and reports API/network errors gracefully

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
  - id: hk_museum_locator
    build: pip install -e .
    path: hk_museum_locator
    inputs:
      user_input: input/user_input
    outputs:
      - museum_locations
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
  - id: input_node
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input

  - id: hk_museum_locator
    build: pip install -e .
    path: hk_museum_locator
    inputs:
      user_input: input_node/user_input
    outputs:
      - museum_locations
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (not used by this node but required for compatibility)
* Metadata:

  ```json
  {
    "dtype": "str"  
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| user_input  | str    | Ignored; required for node-chain compatibility |

### Output Topics

| Topic           | Type  | Description                              |
| --------------- | ----- | ---------------------------------------- |
| museum_locations| dict or list | JSON result from HK GeoData API or error info |


## License

Released under the MIT License.
