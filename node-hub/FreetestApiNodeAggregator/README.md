# freetestapi_node

Aggregate free public API endpoints and deliver normalized results as output in a Dora-rs pipeline.

## Features
- Aggregates data from multiple sample public APIs (airlines, todos, books)
- Graceful error handling per endpoint and overall
- Unified output for any downstream consumer node

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
  - id: freetest-api-aggregator
    build: pip install -e freetestapi_node
    path: freetestapi_node
    inputs:
      user_input: input/user_input
    outputs:
      - api_aggregate_result
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
    build: pip install your-point-source-node
    path: your-point-source-node
    outputs:
      - user_input

  - id: freetest-api-aggregator
    build: pip install -e freetestapi_node
    path: freetestapi_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - api_aggregate_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or trigger value (since agent pulls endpoints internally, the user input is a prompt or trigger)
* Metadata:

  ```json
  {
    "type": "string",
    "purpose": "Trigger aggregation (value ignored)"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                    |
| ------------| ------ | ---------------------------------------------- |
| user_input  | string | Triggers aggregation of all API endpoints      |

### Output Topics

| Topic               | Type    | Description                                 |
| ------------------- | ------- | ------------------------------------------- |
| api_aggregate_result| dict    | Aggregated results from all sample endpoints |


## License

Released under the MIT License.
