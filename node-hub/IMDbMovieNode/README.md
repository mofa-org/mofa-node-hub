# imdb_movie_node

Easily retrieve IMDb movie details or search IMDb movies with a simple Dora-rs node interface.

## Features
- Retrieve full movie metadata by IMDb tt ID
- Search IMDb movies by keyword
- Handles errors gracefully with descriptive messages

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
  - id: imdb_movie_node
    build: pip install -e .
    path: imdb_movie_node
    inputs:
      tt_id: input/tt_id
      query: input/query
    outputs:
      - movie_details
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
  - id: my_query_source
    build: pip install my-query-node
    path: my-query-node
    outputs:
      - query
  - id: imdb_movie_node
    build: pip install -e .
    path: imdb_movie_node
    inputs:
      query: my_query_source/query
    outputs:
      - search_results
```

Your point source must output:

* Topic: `tt_id` or `query`
* Data: string (e.g., 'tt2250912' or 'Spiderman')
* Metadata:

  ```json
  {
    "description": "One of 'tt_id' (IMDb movie tt code) or 'query' (search keyword).",
    "data_type": "string"
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                               |
|---------|--------|-------------------------------------------|
| tt_id   | string | IMDb tt ID (e.g., 'tt2250912')            |
| query   | string | Search string (e.g., 'Spiderman')         |

### Output Topics

| Topic          | Type   | Description                                    |
|----------------|--------|------------------------------------------------|
| movie_details  | object | Movie metadata for provided tt_id              |
| search_results | object | Search response for provided query             |
| error          | object | Error messages with cause and suggestion       |

## License

Released under the MIT License.
