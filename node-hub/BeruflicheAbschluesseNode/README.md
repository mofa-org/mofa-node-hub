# berufliche_abschluesse

Swiss Berufliche Grundbildung Records Fetcher Node for Dora-rs

## Features
- Retrieves Berufliche Grundbildung (vocational training) records from the Swiss public open data API (data.tg.ch)
- Supports fetching either all records or only the most recent records via the `mode` parameter
- Robust error handling with informative error messaging

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
  - id: berufliche_abschluesse
    build: pip install -e .
    path: berufliche_abschluesse
    inputs:
      mode: input/mode         # Optional. Can be omitted to fetch all records.
      user_input: input/user_input # Optional. For chaining with other nodes.
    outputs:
      - records
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
  - id: your_point_source_node
    build: pip install your-point-source
    path: your-point-source-node
    outputs:
      - user_input
      - mode

  - id: berufliche_abschluesse
    build: pip install -e .
    path: berufliche_abschluesse
    inputs:
      user_input: your_point_source_node/user_input
      mode: your_point_source_node/mode
    outputs:
      - records
```

Your point source must output:

* Topic: `user_input` (can be a string or dict, typically used for chaining)
* Topic: `mode` (string: either `all` or `recent`)
* Metadata:

  ```json
  {
    "dtype": "string",  
    "description": "Operation mode. If 'recent', returns the 20 most recent years; otherwise, fetches up to 100 entries."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                                    |
| ----------- | ------ | -------------------------------------------------------------- |
| user_input  | any    | Input parameter to support upstream chaining or custom triggers |
| mode        | string | Fetch mode: 'all' (default, up to 100 results) or 'recent' (20 most recent)|

### Output Topics

| Topic   | Type  | Description                                   |
| ------- | ----- | --------------------------------------------- |
| records | dict  | API response from data.tg.ch, or error message |


## License

Released under the MIT License.
