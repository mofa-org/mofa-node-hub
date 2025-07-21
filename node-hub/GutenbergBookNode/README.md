# gutenberg_book_node

A Dora-rs compatible node that fetches book listings from the Gutenberg Books API, supporting queries for German-language books or copyright-free books via flexible parameters.

## Features
- Query Project Gutenberg's open API for books by German language or copyright status
- Flexible parameter-driven queries ("de" for German, "nocopyright" for copyright-free)
- Handles errors and returns structured JSON output

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
  - id: gutenberg
    build: pip install -e gutenberg_book_node
    path: gutenberg_book_node
    inputs:
      query_type: input/query_type
    outputs:
      - books_output
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
  - id: your_query_node
    build: pip install your-query-node
    path: your-query-node
    outputs:
      - query_type
  - id: gutenberg
    build: pip install -e gutenberg_book_node
    path: gutenberg_book_node
    inputs:
      query_type: your_query_node/query_type
    outputs:
      - books_output
```

Your point source must output:

* Topic: `query_type`
* Data: Parameter string (`"de"` or `"nocopyright"`)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Query type: 'de' for German or 'nocopyright' for copyright-free"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type | Description                                   |
| ---------- | ---- | --------------------------------------------- |
| query_type | str  | Query type, either 'de' for German books or 'nocopyright' for copyright-free books |

### Output Topics

| Topic        | Type  | Description                   |
| ------------ | ----- | ----------------------------- |
| books_output | dict  | JSON results or error details |


## License

Released under the MIT License.
