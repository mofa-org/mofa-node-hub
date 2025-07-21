# country_info_node

Country information retriever node for Dora/MoFA pipeline

## Features
- Retrieve country information by country name
- Lookup country by its capital city
- Robust error handling via distinct output channels

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
  - id: countryinfo
    build: pip install -e country_info_node
    path: country_info_node
    inputs:
      params: input/params # Expects parameters with 'name' or 'capital'
    outputs:
      - country_info_response
      - country_info_error
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
  - id: my_param_source
    build: pip install my-param-source
    path: my_param_source
    outputs:
      - params
  - id: countryinfo
    build: pip install -e country_info_node
    path: country_info_node
    inputs:
      params: my_param_source/params
    outputs:
      - country_info_response
      - country_info_error
```

Your point source must output:

* Topic: `params`
* Data: Dict with 'name' or 'capital' keys
* Metadata:

  ```json
  {
    "fields": ["name", "capital"],
    "required_one_of": ["name", "capital"]
  }
  ```

## API Reference

### Input Topics

| Topic                      | Type            | Description                                                    |
| -------------------------- | --------------- | -------------------------------------------------------------- |
| params                     | dict            | Dictionary with at least one of 'name' or 'capital' string key |

### Output Topics

| Topic                   | Type   | Description                                        |
| ----------------------  | ------ | -------------------------------------------------- |
| country_info_response   | list/dict | Full country information result from RESTCountries  |
| country_info_error      | dict     | Errors, including API errors or missing inputs      |


## License

Released under the MIT License.
