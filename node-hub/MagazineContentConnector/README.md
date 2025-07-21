# magazine_content_connector

A Dora-rs node for querying magazine article content from the [Free Public APIs Magazine API](https://www.freepublicapis.com/magazine-api). It receives filtering parameters (categories, tags, publication_dates) from upstream nodes, fetches magazine article data, and outputs the results for downstream processing or display.

## Features
- Fetches magazine articles using remote HTTP API (Free Public APIs Magazine API)
- Supports filtering by categories, tags, and publication dates
- Outputs JSON-formatted magazine content for consumption by other nodes

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
  - id: magazine_content_connector
    build: pip install -e .
    path: magazine_content_connector
    inputs:
      categories: input/categories
      tags: input/tags
      publication_dates: input/publication_dates
    outputs:
      - magazine_content_data
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
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - categories
      - tags
      - publication_dates
  - id: magazine_content_connector
    build: pip install -e .
    path: magazine_content_connector
    inputs:
      categories: my_input_node/categories
      tags: my_input_node/tags
      publication_dates: my_input_node/publication_dates
    outputs:
      - magazine_content_data
```

Your point source must output:

* Topic: `categories`, `tags`, `publication_dates`
* Data: String values (comma-separated if multiple)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "String value or comma-separated list as input filter"
  }
  ```

## API Reference

### Input Topics

| Topic              | Type   | Description |
|--------------------|--------|-------------|
| categories         | str    | Comma-separated category names (e.g., "tech,travel") |
| tags               | str    | Comma-separated tag list (e.g., "open-source,2024") |
| publication_dates  | str    | Date or date range (e.g., "2024-01-01,2024-03-01") |

### Output Topics

| Topic                  | Type   | Description |
|------------------------|--------|-------------|
| magazine_content_data  | dict or list | Magazine API articles as JSON (or error message as dict) |


## License

Released under the MIT License.
