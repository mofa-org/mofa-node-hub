# beer_api_node

A Dora-rs node that provides programmatic access to the PunkAPI (v3), allowing you to list beers, fetch beers by ID, or retrieve a random beer from the PunkAPI database. This node is ideal for integrating beer data into Dora pipelines, demos, or explorations.

## Features
- List beers (by page)
- Fetch beer by specific ID
- Retrieve a random beer

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
  - id: beer_api_node
    build: pip install -e .
    path: beer_api_node
    inputs:
      parameters: input/parameters
    outputs:
      - api_response
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
  - id: my_control_node
    outputs:
      - parameters
  - id: beer_api_node
    build: pip install -e .
    path: beer_api_node
    inputs:
      parameters: my_control_node/parameters
    outputs:
      - api_response
      - error
```

Your point source must output:

* Topic: `parameters`
* Data: Dict with keys 'operation' and optional 'value'
* Metadata:

  ```json
  {
    "operation": "list | random | by_id", 
    "value": "page number for list, id for by_id, or ''"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type                | Description                             |
| ----------- | ------------------- | --------------------------------------- |
| parameters  | dict (str:str)      | Control dict with 'operation' and 'value'. |

### Output Topics

| Topic        | Type      | Description                                        |
| ------------ | --------- | -------------------------------------------------- |
| api_response | str (JSON)| The API response (JSON-encoded string)              |
| error        | str       | Error message if the API call or parameters fail    |


## License

Released under the MIT License.
