# water_quality_node

Fetch UK water quality sampling points via the DEFRA Water Quality Archive API.

## Features
- Query DEFRA Water Quality Archive for sampling points
- Dynamic term search via Dora parameters
- API error and connection handling

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: water_quality_node
    build: pip install -e .
    path: water_quality_node
    inputs:
      search: input/search  # Optional parameter; defaults to 'clifton'
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
    # ...
    outputs:
      - search  # Should output the search term (e.g., 'clifton')
  - id: water_quality_node
    build: pip install -e .
    path: water_quality_node
    inputs:
      search: my_input_node/search
    outputs:
      - api_response
```

Your point source must output:

* Topic: `search`
* Data: String with your search term
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "Search term to query DEFRA water quality API"
  }
  ```

## API Reference

### Input Topics

| Topic  | Type   | Description                                  |
| ------ | ------ | -------------------------------------------- |
| search | string | Search string for DEFRA sampling point query |

### Output Topics

| Topic        | Type  | Description                  |
| ------------ | ----- | --------------------------- |
| api_response | dict  | DEFRA API JSON response     |


## License

Released under the MIT License.
