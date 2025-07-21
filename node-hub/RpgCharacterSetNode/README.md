# rpg_character_set

Random RPG Character and Set Generator Node

## Features
- Fetches a random RPG character from set.world API
- Fetches a random RPG item set from set.world API
- Provides error handling and structured error outputs

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
  - id: rpg-character-set
    build: pip install -e .
    path: rpg_character_set
    inputs:
      user_input: input/user_input  # Optional/placeholder input
    outputs:
      - character
      - item_set
      - error
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
  - id: my-point-source
    build: pip install -e my-point-source
    path: my_point_source
    outputs:
      - user_input
  - id: rpg-character-set
    build: pip install -e .
    path: rpg_character_set
    inputs:
      user_input: my-point-source/user_input
    outputs:
      - character
      - item_set
      - error
```

Your point source must output:

* Topic: `user_input`
* Data: Any JSON-serializable object (unused, placeholder for pipeline consistency)
* Metadata:

  ```json
  {
    "description": "Placeholder input; not used by this node."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                             |
| ----------- | ------ | --------------------------------------- |
| user_input  | Any    | Placeholder parameter for compatibility |

### Output Topics

| Topic      | Type | Description                                |
| ---------- | ---- | ------------------------------------------ |
| character  | JSON | Random RPG character from set.world API    |
| item_set   | JSON | Random item set from set.world API         |
| error      | JSON | Error messages and description             |


## License

Released under the MIT License.
