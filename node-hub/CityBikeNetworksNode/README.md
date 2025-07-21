# citybike_networks_node

CityBikeNetworksNode: Dora node for retrieving city bike network data worldwide via citybik.es API.

## Features
- Fetches summary of all city bike networks and their URLs with selected fields
- Retrieves the entire city bike networks dataset (global coverage)
- Robust error handling and JSON serializability checks

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
  - id: citybike_node
    build: pip install -e .
    path: citybike_networks_node
    inputs:
      user_input: input/user_input
    outputs:
      - selected_fields_networks
      - all_networks
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
  - id: external_source
    build: pip install your-external-node  # Example source producing user_input
    path: your-external-node
    outputs:
      - user_input

  - id: citybike_node
    build: pip install -e .
    path: citybike_networks_node
    inputs:
      user_input: external_source/user_input
    outputs:
      - selected_fields_networks
      - all_networks
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy or empty OK)
* Metadata:

  ```json
  {
    "type": "object",
    "description": "Trigger for citybike query."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                       |
| ----------| ------- | --------------------------------- |
| user_input | object  | Triggers a refresh of the bike network data |

### Output Topics

| Topic                    | Type    | Description                                                      |
| ------------------------ | ------- | ---------------------------------------------------------------- |
| selected_fields_networks | object  | List/dict with 'id', 'name', 'href' for all city bike networks   |
| all_networks             | object  | The full city bike networks dataset (all metadata and coverage)   |


## License

Released under the MIT License.
