# MetMuseumCollectionNode

A Dora node to query the Metropolitan Museum of Art's public collection API. Retrieve department listings, or search for objects via keyword from any pipeline.

## Features
- List all departments in the Metropolitan Museum of Art collection
- Search for objects by keyword
- Structured error reporting via an output port

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
  - id: metmuseum
    build: pip install -e met_museum_node
    path: met_museum_node
    inputs:
      parameters: input/parameters
    outputs:
      - departments
      - search_results
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
  - id: param_source
    build: pip install your-parameter-source
    path: your-parameter-source
    outputs:
      - parameters

  - id: metmuseum
    build: pip install -e met_museum_node
    path: met_museum_node
    inputs:
      parameters: param_source/parameters
    outputs:
      - departments
      - search_results
      - error
```

Your point source must output:

* Topic: `parameters`
* Data: Must be a dict with fields:

  ```json
  {
    "action": "departments" | "search", // String: operation to perform
    "query": ""  // String: search term (only required with action='search')
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                 |
| ----------- | ------ | ------------------------------------------- |
| parameters  | dict   | Contains `action` (string) and `query` (string) |

### Output Topics

| Topic          | Type   | Description                                          |
| -------------- | ------ | ---------------------------------------------------- |
| departments    | dict   | Output of department listing from the Met Museum API |
| search_results | dict   | Output of search results from the Met Museum API     |
| error          | dict   | Errors and exceptions (with a `message` field)       |


## License

Released under the MIT License.
