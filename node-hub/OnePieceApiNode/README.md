# onepiece_api_node

A Dora-rs node for querying public One Piece anime API endpoints. Allows downstream pipeline nodes to fetch sagas, characters, or devil fruits from the open API by specifying the resource.

## Features
- Fetch data on One Piece sagas, characters, or fruits from public API
- Timeout control via input parameter for HTTP requests
- Returns structured API results (success/error)

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
  - id: onepiece_api_node
    build: pip install -e .
    path: onepiece_api_node
    inputs:
      user_input: input/user_input # unused, but required by node interface
      resource: input/resource    # one of 'sagas', 'characters', 'fruits'
      timeout: input/timeout      # optional, int seconds
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
  - id: your_query_node
    build: pip install -e .
    path: your_query_node
    outputs:
      - resource
      - user_input
      - timeout

  - id: onepiece_api_node
    build: pip install -e .
    path: onepiece_api_node
    inputs:
      user_input: your_query_node/user_input
      resource: your_query_node/resource
      timeout: your_query_node/timeout
    outputs:
      - api_response
  # Other nodes can consume 'api_response' from here
```

Your point source must output:

* Topic: `resource`
* Data: String value, one of `sagas`, `characters`, or `fruits`.
* Metadata:

  ```json
  {
    "description": "Resource type to fetch (sagas, characters, fruits)",
    "type": "string",
    "allowed": ["sagas", "characters", "fruits"]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                |
|------------|--------|--------------------------------------------|
| user_input | string | Not used, placeholder for compatibility    |
| resource   | string | Resource to fetch: 'sagas', 'characters', or 'fruits' |
| timeout    | int    | (Optional) HTTP request timeout, in seconds|

### Output Topics

| Topic        | Type   | Description         |
|--------------|--------|--------------------|
| api_response | dict   | Result from the API (success/data or error) |


## License

Released under the MIT License.
