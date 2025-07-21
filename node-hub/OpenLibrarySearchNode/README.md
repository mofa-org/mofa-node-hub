# openlibrary_search

Search OpenLibrary for Books by Title or Author

## Features
- Search books by title or author using OpenLibrary's REST API
- Supports optional sorting when searching by author
- Outputs detailed JSON search results compatible with Dora/Mofa messaging

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
  - id: openlibrary_search
    build: pip install -e .
    path: openlibrary_search
    inputs:
      parameters: input/parameters
    outputs:
      - openlibrary_results
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
  - id: your_input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - parameters

  - id: openlibrary_search
    build: pip install -e .
    path: openlibrary_search
    inputs:
      parameters: your_input_node/parameters
    outputs:
      - openlibrary_results
```

Your point source must output:

* Topic: `parameters`
* Data: Dictionary or object with keys: `operation`, `query`, `sort` (all strings, `sort` optional)
* Metadata:

  ```json
  {
    "operation": "title_search | author_search",
    "query": "<search string>",
    "sort": "<sort order, optional>"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                     |
| ---------- | ------ | ------------------------------- |
| parameters | dict   | Operation/query/sort parameters |

### Output Topics

| Topic              | Type | Description                        |
| ------------------ | ---- | ---------------------------------  |
| openlibrary_results | dict | JSON results from OpenLibrary API  |


## License

Released under the MIT License.
