# DisneyCharacterNode

A Dora-rs node that retrieves Disney character information by ID, name, or lists all available characters using the https://api.disneyapi.dev REST API. The node interfaces through input and output ports for integration into Dora pipelines and tools.

## Features
- Fetch character details by unique ID
- Search characters by name
- Retrieve and list all Disney characters via API

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
  - id: disney_query
    build: pip install -e disney_character_node
    path: disney_character_node
    inputs:
      action: input/action
      value: input/value
    outputs:
      - result
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
  - id: my_custom_input
    build: pip install your-custom-input
    path: your-custom-input
    outputs:
      - action
      - value

  - id: disney_query
    build: pip install -e disney_character_node
    path: disney_character_node
    inputs:
      action: my_custom_input/action
      value: my_custom_input/value
    outputs:
      - result

  - id: display
    build: pip install dora-rerun
    path: dora-rerun
    inputs:
      result: disney_query/result
```

Your point source must output:

* Topic: `action`
* Data: String (must be one of: 'by_id', 'by_name', 'all')
* Metadata:

  ```json
  {
    "type": "string",
    "allowed_values": ["by_id", "by_name", "all"],
    "description": "Query action: fetch by id, by name or all characters"
  }
  ```

* Topic: `value`
* Data: String (required for 'by_id' and 'by_name')
* Metadata:
  ```json
  {
    "type": "string",
    "description": "The ID or name parameter, depending on selected action"
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                                              |
| ------- | ------ | ------------------------------------------------------- |
| action  | String | Query type: 'by_id', 'by_name', 'all'                   |
| value   | String | The ID or name parameter (required for by_id/by_name)   |

### Output Topics

| Topic  | Type       | Description                                   |
| ------ | ---------- | --------------------------------------------- |
| result | dict/string | API response as dict or error message string  |


## License

Released under the MIT License.
