# amiibo_character_node

Fetch Amiibo Character Metadata Node

## Features
- Retrieves Amiibo character information via the [amiiboapi.com](https://www.amiiboapi.com/) HTTP API
- Accepts character names dynamically through the pipeline or fallback parameters
- Outputs Amiibo metadata in structured format for easy downstream integration

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
  - id: amiibo_character_node
    build: pip install -e amiibo_character_node
    path: amiibo_character_node
    inputs:
      name: input/name
      user_input: input/user_input
    outputs:
      - amiibo_character_info
    env: {}
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
  - id: your_point_source
    build: pip install your-node
    path: your-point-source-node
    outputs:
      - name

  - id: amiibo_character_node
    build: pip install -e amiibo_character_node
    path: amiibo_character_node
    inputs:
      name: your_point_source/name
      user_input: input/user_input
    outputs:
      - amiibo_character_info
```

Your point source must output:

* Topic: `name`
* Data: (string) Amiibo character name
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Amiibo character name (e.g. 'mario', 'link', etc.)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| user_input  | any    | User-provided input for flexibility            |
| name        | str    | Name of the Amiibo character (eg. 'mario')     |

### Output Topics

| Topic                   | Type            | Description                                  |
| ----------------------- | --------------- | -------------------------------------------- |
| amiibo_character_info   | dict (JSON)     | Amiibo character metadata from Amiibo API     |


## License

Released under the MIT License.
