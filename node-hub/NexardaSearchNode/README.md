# nexarda_search_node

Nexarda video game search Dora node

## Features
- Search NEXARDA™ for video games using a public API
- Easy integration—just provide a search query, get structured results
- Robust error handling with informative error output

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
  - id: nexarda_search
    build: pip install -e nexarda_search_node
    path: nexarda_search_node
    inputs:
      query: input/query
    outputs:
      - search_results
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
  - id: my_query_node
    path: my_query_node
    outputs:
      - query

  - id: nexarda_search
    build: pip install -e nexarda_search_node
    path: nexarda_search_node
    inputs:
      query: my_query_node/query
    outputs:
      - search_results
```

Your point source must output:

* Topic: `query`
* Data: string containing the game search query
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Video game search query for NEXARDA API"
  }
  ```

## API Reference

### Input Topics

| Topic | Type | Description |
|-------|------|-------------|
| query | str  | Video game search query (defaults to 'Example Game' if empty) |

### Output Topics

| Topic          | Type         | Description               |
|--------------- |------------- |-------------------------- |
| search_results | dict/list/str| Results from NEXARDA API  |


## License

Released under the MIT License.
