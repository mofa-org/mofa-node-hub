# place_of_worship_node

A Dora-rs node providing access to place-of-worship information via the OpenSanctum API. Supports both church and religion entity queries with robust error handling and parameterized inputs.

## Features
- Query OpenSanctum API for detailed data on churches or religions
- Handles dynamic input parameters for flexible API usage
- Robust error and retry logic for reliable remote calls

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
  - id: place_of_worship_api
    build: pip install -e .
    path: place_of_worship_node
    inputs:
      query_type: input/query_type
      entity_id: input/entity_id
    outputs:
      - api_response
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
    build: pip install -e my-input-node
    path: my_input_node
    outputs:
      - query_type
      - entity_id

  - id: place_of_worship_api
    build: pip install -e .
    path: place_of_worship_node
    inputs:
      query_type: my_input_node/query_type
      entity_id: my_input_node/entity_id
    outputs:
      - api_response
```

Your point source must output:

* Topic: `query_type` (string: "church" or "religion")
* Topic: `entity_id` (string/integer, should be integer as string is parsed to int)
* Metadata:

  ```json
  {
    "query_type": "church",
    "entity_id": "42"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                         |
| ------------| ------ | ----------------------------------- |
| query_type  | string | Type of entity to query: 'church' or 'religion' |
| entity_id   | string | ID of the entity to look up (integer as string) |

### Output Topics

| Topic        | Type                | Description                          |
| ------------ | ------------------ | ------------------------------------ |
| api_response | dict (JSON object)  | API result or error message          |


## License

Released under the MIT License.
