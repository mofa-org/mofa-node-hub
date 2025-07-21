# spanish_fuel_node

A Dora-rs node for retrieving open Spanish government fuel dataset listings from datos.gob.es and streaming them as structured messages. Handles HTTP, JSON, and error reporting for robust pipeline integration.

## Features
- Fetches top 10 Spanish open dataset entries from datos.gob.es
- Robust error reporting (HTTP and JSON parsing errors)
- Simple integration with Mofa pipeline and other Dora nodes

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
  - id: spanish_fuel_node
    build: pip install -e .
    path: spanish_fuel_node
    outputs:
      - fuel_dataset
      - api_error
      - node_error
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
  - id: dataset_fetcher
    build: pip install -e .
    path: spanish_fuel_node
    outputs:
      - fuel_dataset
      - api_error
  - id: your_next_node
    build: pip install -e your-next-node
    path: your-next-node
    inputs:
      dataset: dataset_fetcher/fuel_dataset
      errors: dataset_fetcher/api_error
```

Your point source must output:

* Topic: `points_to_track`
* Data: Flattened array of coordinates
* Metadata:

  ```json
  {
    "num_points": 10,
    "dtype": "float32",
    "shape": [10, 2]
  }
  ```

## API Reference

### Input Topics

| Topic              | Type       | Description                  |
| ------------------ | ----------| ---------------------------- |
| user_input         | any       | Reserved for future use      |

### Output Topics

| Topic          | Type   | Description                        |
| -------------- | -----  | ---------------------------------- |
| fuel_dataset   | dict   | JSON data from datos.gob.es API    |
| api_error      | dict   | Errors relating to HTTP/API access |
| node_error     | dict   | Unexpected node-level errors       |


## License

Released under the MIT License.
