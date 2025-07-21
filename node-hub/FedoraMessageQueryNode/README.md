# fedora_query_node

Query Fedora Messaging historical messages via HTTP API for use within Dora-rs or MOFA agent pipelines.

## Features
- Query Fedora messages history with flexible parameters
- Data-driven and dynamic API payload configuration
- Robust error handling with serializable outputs

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
  - id: fedora_query_node
    build: pip install -e .
    path: fedora_query_node
    inputs:
      username: input/username
      package: input/package
      source: input/source
      topic: input/topic
      page: input/page
      rows_per_page: input/rows_per_page
    outputs:
      - results
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
  - id: point_source
    outputs:
      - username
      - package
      - source
      - topic
      - page
      - rows_per_page
  - id: fedora_query_node
    build: pip install -e .
    path: fedora_query_node
    inputs:
      username: point_source/username
      package: point_source/package
      source: point_source/source
      topic: point_source/topic
      page: point_source/page
      rows_per_page: point_source/rows_per_page
    outputs:
      - results
```

Your point source must output:

* Topic: `username`, `package`, `source`, `topic`, `page`, `rows_per_page`
* Data: string or integer (as strings)
* Metadata:

  ```json
  {
    "type": "string",
    "optional": true
  }
  ```

## API Reference

### Input Topics

| Topic           | Type    | Description                                                        |
| --------------- | ------- | ------------------------------------------------------------------ |
| username        | string  | Username for filtering Fedora messages (optional)                  |
| package         | string  | Package name for query (optional)                                  |
| source          | string  | Message source (optional)                                          |
| topic           | string  | Fedora message topic (optional)                                    |
| page            | string  | Page number for pagination (optional; will be converted to integer)|
| rows_per_page   | string  | Number of rows per page (optional; will be converted to integer)   |

### Output Topics

| Topic    | Type | Description                               |
|----------|------|-------------------------------------------|
| results  | dict | API response from Fedora datagrepper query |


## License

Released under the MIT License.
