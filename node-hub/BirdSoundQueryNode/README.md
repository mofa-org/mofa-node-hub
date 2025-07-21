# bird_sound_query

Query Xeno-Canto for Bird Sound Recordings from Dora-rs

## Features
- Query bird sound recordings from the Xeno-Canto API using flexible natural language search.
- Handles errors gracefully by returning an error message on a separate output port.
- Simple integration as a stateless Dora node with fast setup and no dependencies beyond Python `requests`.

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
  - id: bird_sound_query
    build: pip install -e .
    path: bird_sound_query
    inputs:
      query: input/query
    outputs:
      - bird_sounds
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
    build: pip install my-query-source
    path: my_query_source
    outputs:
      - query

  - id: bird_sound_query
    build: pip install -e .
    path: bird_sound_query
    inputs:
      query: my_query_source/query
    outputs:
      - bird_sounds
      - error
```

Your point source must output:

* Topic: `query`
* Data: String query, e.g. `'troglodytes troglodytes'` or `'cnt:brazil'`
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Any valid Xeno-Canto search query, see https://www.xeno-canto.org/help/search"
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                                  |
| ------- | ------ | -------------------------------------------- |
| query   | str    | Xeno-Canto API search (e.g. bird name, region) |

### Output Topics

| Topic       | Type | Description                                 |
| ----------- | ---- | ------------------------------------------- |
| bird_sounds | dict | Xeno-Canto result (including recordings)    |
| error       | dict | Error information for failed queries        |


## License

Released under the MIT License.
