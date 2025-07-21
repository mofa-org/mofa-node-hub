# fruit_lookup_node

Fruit information lookup node for Dora-rs (MofaAgent powered)

## Features
- Fetches detailed banana information via an external API
- Retrieves information for all available fruits
- Simple output integration into Dora/Mofa pipelines

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
  - id: fruit_lookup
    build: pip install -e .
    path: fruit_lookup_node
    inputs:
      user_input: input/user_input
    outputs:
      - banana_info
      - all_fruits_info
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
  - id: your_node
    build: pip install -e .
    path: your_node
    outputs:
      - user_input

  - id: fruit_lookup
    build: pip install -e .
    path: fruit_lookup_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - banana_info
      - all_fruits_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (not used by this node, only required for compliance)
* Metadata:

  ```json
  {
    "description": "Arbitrary user input; can be empty or any serializable value."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type           | Description        |
| ----------- | -------------- | ------------------|
| user_input  | any (optional) | Placeholder input; not used, but required for compliance |

### Output Topics

| Topic           | Type  | Description                                         |
| --------------- | ----- | ---------------------------------------------------|
| banana_info     | dict  | API response containing banana information          |
| all_fruits_info | list  | API response containing all fruits information      |


## License

Released under the MIT License.
