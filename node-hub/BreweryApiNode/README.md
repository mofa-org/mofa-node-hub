# BreweryApiNode

Query the OpenBreweryDB API via a Dora node agent interface.

## Features
- Fetch the full list of breweries (OpenBreweryDB `/breweries` endpoint)
- Fetch a single brewery by ID (OpenBreweryDB `/breweries/{id}` endpoint)
- Simple Python interface with parameterizable API queries

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
  - id: brewery_api_node
    build: pip install -e .
    path: .
    inputs:
      endpoint_type: input/endpoint_type
      brewery_id: input/brewery_id
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
  - id: my_endpoint_node
    build: pip install my-source
    path: my-endpoint-node
    outputs:
      - endpoint_type
      - brewery_id

  - id: brewery_api_node
    build: pip install -e .
    path: .
    inputs:
      endpoint_type: my_endpoint_node/endpoint_type
      brewery_id: my_endpoint_node/brewery_id
    outputs:
      - api_response

  - id: response_sink
    build: pip install dora-rerun
    path: dora-rerun
    inputs:
      api_response: brewery_api_node/api_response
```

Your point source must output:

* Topic: `endpoint_type` and optionally `brewery_id`
* Data: For `endpoint_type`, expects string: `"list"` or `"single"`. For `brewery_id`, expects a string OpenBreweryDB brewery ID (when `endpoint_type` is `"single"`).
* Metadata:

  ```json
  {
    "type": "string",
    "required": true,
    "description": "API endpoint selection. 'list' for all breweries, 'single' for a single brewery. If 'single', you must also supply 'brewery_id' as a string."
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                                                                        |
| --------------- | ------ | ---------------------------------------------------------------------------------- |
| endpoint_type   | string | Required. Must be either 'list' or 'single'. Selects which OpenBreweryDB endpoint. |
| brewery_id      | string | Required only if endpoint_type is 'single': the ID for a single brewery.            |

### Output Topics

| Topic        | Type         | Description                                                   |
| ------------ | ------------ | ------------------------------------------------------------- |
| api_response | dict or list | JSON response from OpenBreweryDB, or error as a dictionary.   |


## License

Released under the MIT License.
