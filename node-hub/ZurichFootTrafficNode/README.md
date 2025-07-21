# zurich_foot_traffic

Agent for querying Zurich public foot traffic data endpoints with simple operations.

## Features
- Fetch latest Zurich foot traffic records easily
- Search for Jones-related records in Zurich's database
- Robust error handling for invalid operations and HTTP issues

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
  - id: zurich_foot_traffic_node
    build: pip install -e .
    path: zurich_foot_traffic
    inputs:
      operation: input/operation
    outputs:
      - output_port
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
  - id: my_node
    build: pip install -e my_node
    path: my_node
    outputs:
      - operation

  - id: zurich_foot_traffic_node
    build: pip install -e .
    path: zurich_foot_traffic
    inputs:
      operation: my_node/operation
    outputs:
      - output_port
```

Your point source must output:

* Topic: `operation`
* Data: string, either `search_jones` or `fetch_latest`
* Metadata:

  ```json
  {
    "type": "str",
    "enum": ["search_jones", "fetch_latest"]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type | Description                                    |
| ----------|------|------------------------------------------------|
| operation | str  | Query to run: 'search_jones' or 'fetch_latest' |

### Output Topics

| Topic       | Type | Description                                  |
|-------------|------|----------------------------------------------|
| output_port | dict | Response from Zurich endpoint, or error info  |

## License

Released under the MIT License.
