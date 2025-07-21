# bird_api_node

Retrieve bird species data from the FreeTestAPI and flexibly query by keyword using Dora/Mofa message passing.

## Features
- Query a live bird species REST API and relay structured results
'through Dora/Mofa outputs
- Flexible parameter-based filtering (search by keyword/phrase)
- Compatible with broader Dora/Mofa pipelines for dynamic integration

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
  - id: bird_api_node
    build: pip install -e .
    path: bird_api_node
    inputs:
      user_input: input/user_input
      search: input/search
    outputs:
      - birds_result
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
  - id: my_custom_ui
    # ...
    outputs:
      - search
  - id: bird_api_node
    build: pip install -e .
    path: bird_api_node
    inputs:
      search: my_custom_ui/search
    outputs:
      - birds_result
```

Your point source must output:

* Topic: `search`
* Data: String (search keyword or empty)
* Metadata:

  ```json
  {
    "type": "str",
    "description": "Search keyword to filter bird species or empty for all birds"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                              |
| ----------- | ------ | ---------------------------------------- |
| user_input  | any    | Auxiliary parameter (for dataflow/unused) |
| search      | str    | Search keyword for querying bird species  |

### Output Topics

| Topic         | Type   | Description                                           |
| ------------- | ------ | ----------------------------------------------------- |
| birds_result  | dict   | Result list of birds from API or error information    |


## License

Released under the MIT License.
