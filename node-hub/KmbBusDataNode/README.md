# kmb_bus_node

Hong Kong KMB Bus Routes/Stops Fetch Node

## Features
- Fetches all KMB bus routes and stops from Hong Kong's ETA Bus open API
- Outputs a single comprehensive dictionary with routes and stops
- Handles network/API errors internally and emits error messages as part of output

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
  - id: kmb_bus_data
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input
    outputs:
      - kmb_bus_data
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
  - id: kmb_bus_data
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input
    outputs:
      - kmb_bus_data

  # Example downstream consumer
  - id: your_consumer_node
    build: pip install your-consumer-package
    path: your-consumer-node-path
    inputs:
      kmb_bus_data: kmb_bus_data/kmb_bus_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any parameter (string or structured), used as a placeholder to trigger fetch
* Metadata:

  ```json
  {
    "description": "User trigger or options for KMB data node (not used, placeholder)"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                   |
| ------------|--------|-----------------------------------------------|
| user_input  | object | Placeholder trigger; any input triggers fetch. |

### Output Topics

| Topic         | Type      | Description                                                             |
|-------------- |-----------|-------------------------------------------------------------------------|
| kmb_bus_data | dict      | Contains keys: 'routes', 'stops' (API data), and 'error' (if any error). |


## License

Released under the MIT License.
