# monster_hunter_node

A Dora-rs node providing Monster Hunter World data aggregation through the mhw-db.com API. Fetches monsters, armor, and ailments data for downstream nodes via a single endpoint.

## Features
- Aggregates Monster Hunter World data from mhw-db.com
- Exposes a single unified output with monster, armor, and ailments info
- Handles HTTP errors and JSON parsing robustly

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
  - id: monster_hunter_node
    build: pip install -e .
    path: monster_hunter_node
    inputs:
      user_input: input/user_input
    outputs:
      - mhworld_info
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
  - id: user_source
    build: pip install my-user-source
    path: my-user-source
    outputs:
      - user_input

  - id: monster_hunter_node
    build: pip install -e .
    path: monster_hunter_node
    inputs:
      user_input: user_source/user_input
    outputs:
      - mhworld_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (user prompt or configuration)
* Metadata:
  ```json
  {"description": "User prompt or config string for MHW queries"}
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                             |
| ----------- | ------ | --------------------------------------- |
| user_input  | str    | User input string for downstream logic  |

### Output Topics

| Topic         | Type   | Description                                                       |
| ------------- | ------ | ------------------------------------------------------------------ |
| mhworld_info  | dict   | Aggregated data with 'monsters', 'armor', and 'ailments' sections  |

## License

Released under the MIT License.
