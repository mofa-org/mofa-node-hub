# scryfall_set_node

Retrieve Scryfall Aether Revolt Set Metadata with Dora-rs

## Features
- Fetches Aether Revolt set metadata from the Scryfall API
- Dora-rs compliant node with automatic output serialization
- Error reporting in API responses

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
  - id: scryfall_set_retriever
    build: pip install -e .
    path: scryfall_set_node
    inputs:
      user_input: input/user_input
    outputs:
      - scryfall_set_data
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
  - id: my_point_source
    build: pip install my-point-source
    path: my_point_source
    outputs:
      - user_input
  - id: scryfall_set_retriever
    build: pip install -e .
    path: scryfall_set_node
    inputs:
      user_input: my_point_source/user_input
    outputs:
      - scryfall_set_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (not used)
* Metadata:

  ```json
  {"description": "Any placeholder value; not used by scryfall_set_node"}
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                          |
| ----------- | ------- | ---------------------------------------------------- |
| user_input  | Any     | Placeholder input topic for triggering agent action. |

### Output Topics

| Topic              | Type   | Description                                                |
| ------------------ | ------ | ---------------------------------------------------------- |
| scryfall_set_data  | dict   | Scryfall Aether Revolt set data (or error info as a dict). |


## License

Released under the MIT License.
