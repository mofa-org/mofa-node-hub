# npm_registry_node

Node for Fetching and Searching npm Registry

## Features
- Retrieve detailed package metadata from the npm registry
- Search for packages on npm by name or keyword
- Provides unified output including error handling

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
  - id: npm_registry
    build: pip install -e npm_registry_node
    path: npm_registry_node
    inputs:
      user_input: input/user_query
    outputs:
      - npm_registry_data
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
  - id: my_input_node
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - user_query

  - id: npm_registry
    build: pip install -e npm_registry_node
    path: npm_registry_node
    inputs:
      user_input: my_input_node/user_query
    outputs:
      - npm_registry_data

  - id: my_display_node
    build: pip install my-display-node
    path: my_display_node
    inputs:
      npm_registry_data: npm_registry/npm_registry_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any type or string representing the search term (can be ignored by this node)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "User query for npm search (optional, not required or used)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| user_input  | string | User input for search (received but ignored) |

### Output Topics

| Topic             | Type           | Description                                      |
| ----------------- | -------------- | ------------------------------------------------ |
| npm_registry_data | dict/object    | npm registry package info and search, plus errors |


## License

Released under the MIT License.
