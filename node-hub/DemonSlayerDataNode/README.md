# demon_slayer_node

Fetch Demon Slayer Universe Data via MOFA Agent Node

## Features
- Dynamically fetches Demon Slayer characters or combat styles from public API
- Flexible selection of data type through node parameter
- Graceful error handling with detailed messages

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
  - id: demon_slayer_node
    build: pip install -e .
    path: demon_slayer_node
    inputs:
      data_type: input/data_type
    outputs:
      - demon_slayer_data
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
  - id: your_input_node
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - data_type

  - id: demon_slayer_node
    build: pip install -e .
    path: demon_slayer_node
    inputs:
      data_type: your_input_node/data_type
    outputs:
      - demon_slayer_data
```

Your point source must output:

* Topic: `data_type`
* Data: string (either "characters" or "combat_styles")
* Metadata:

  ```json
  {
    "description": "Specifies whether to fetch Demon Slayer characters or combat styles.",
    "valid_values": ["characters", "combat_styles"]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                      |
| ---------- | ------ | ------------------------------------------------ |
| data_type  | str    | Either 'characters' or 'combat_styles' to select Demon Slayer API endpoint |

### Output Topics

| Topic              | Type   | Description                                                                    |
| ------------------ | ------ | ------------------------------------------------------------------------------ |
| demon_slayer_data  | dict   | API response: a list of characters/combat styles, or error message on failure   |


## License

Released under the MIT License.
