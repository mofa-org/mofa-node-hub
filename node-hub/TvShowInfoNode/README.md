# tvshow_info_node

Query TVMaze API for show search results and Big Bang Theory images via Dora-rs compatible node.

## Features
- Search for TV show information using TVMaze API
- Retrieve all images for 'The Big Bang Theory' (static fetch)
- Receive search query as an input parameter and output diagnostic/error information

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
  - id: tv_info
    build: pip install -e .
    path: tvshow_info_node
    inputs:
      show_query: input/show_query
    outputs:
      - search_results
      - big_bang_images
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
  - id: user_query
    build: pip install my-user-query-node
    path: my-user-query-node
    outputs:
      - show_query

  - id: tv_info
    build: pip install -e .
    path: tvshow_info_node
    inputs:
      show_query: user_query/show_query
    outputs:
      - search_results
      - big_bang_images
```

Your point source must output:

* Topic: `show_query`
* Data: Show search string (UTF-8 encoded, or plain string)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Search query string for TV show. Example: 'Friends'"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                   |
|-------------|--------|-------------------------------|
| show_query  | str    | Search query for TV show name |

### Output Topics

| Topic            | Type         | Description                                        |
|------------------|--------------|----------------------------------------------------|
| search_results   | dict/list    | TVMaze API search results for queried show          |
| big_bang_images  | dict/list    | Image assets for show 'The Big Bang Theory'        |

## License

Released under the MIT License.
