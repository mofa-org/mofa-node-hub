# pokemon_tcg_node

A Dora-rs node that retrieves Yu-Gi-Oh! trading card data from the online YGOPRODECK API. Flexible filter support allows programmatic querying by card attributes via Dora message ports.

## Features
- Query Yu-Gi-Oh! card details from the public YGOPRODECK API
- Dynamic filter support via JSON or query string message
- Robust error handling and API timeout safety

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
  - id: pokemon-tcg
    build: pip install -e .
    path: pokemon_tcg_node
    inputs:
      filter_params: input/filter_params
      user_input: input/user_input
    outputs:
      - card_data
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
  - id: custom-filter
    build: pip install my-filter-node
    path: my_filter_node
    outputs:
      - filter_params
  - id: pokemon-tcg
    build: pip install -e .
    path: pokemon_tcg_node
    inputs:
      filter_params: custom-filter/filter_params
      user_input: input/user_input
    outputs:
      - card_data
```

Your point source must output:

* Topic: `filter_params`
* Data: String (JSON dict or url-encoded query string, e.g. '{"race":"Fiend"}' or 'race=Fiend')
* Metadata:

  ```json
  {
    "type": "string",
    "description": "JSON dict or URL query string for filtering card API requests."
  }
  ```

## API Reference

### Input Topics

| Topic          | Type   | Description                                                        |
| --------------| ------ | ------------------------------------------------------------------ |
| filter_params  | string | Optional. Filter query as JSON or query-string (e.g. 'race=Fiend') |
| user_input     | string | Optional. Receives a signal or user input if needed                |

### Output Topics

| Topic      | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| card_data  | dict or list  | Card data response from API   |


## License

Released under the MIT License.
