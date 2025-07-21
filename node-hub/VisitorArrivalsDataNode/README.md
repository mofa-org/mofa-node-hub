# visitor_arrivals_node

Fetch official Hong Kong visitor arrivals data for Dora pipelines via a simple agent node.

## Features
- Retrieves visitor arrivals time-series data from the Hong Kong Census & Statistics Department API
- Returns structured JSON output for downstream usage
- Handles error conditions gracefully (API failure, malformed responses, timeouts)

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
  - id: visitor_arrivals_node
    build: pip install -e .
    path: visitor_arrivals_node
    inputs:
      user_input: input/user_input
    outputs:
      - visitor_arrivals_data
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
  - id: your_point_source
    build: pip install your-point-source
    path: your-point-source
    outputs:
      - user_input
  - id: visitor_arrivals_node
    build: pip install -e .
    path: visitor_arrivals_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - visitor_arrivals_data
      - error
```

Your point source must output:

* Topic: `user_input`
* Data: Any placeholder (required for execution, can be null or empty string)
* Metadata:

  ```json
  {
    "description": "Trigger for data fetch. Value is ignored."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                             |
| ----------- | -------- | --------------------------------------- |
| user_input  | Any      | Placeholder to trigger data fetch       |

### Output Topics

| Topic                 | Type   | Description                           |
| --------------------- | ------ | ------------------------------------- |
| visitor_arrivals_data | JSON   | Visitor arrivals dataset from API     |
| error                 | JSON   | Error information if query fails      |


## License

Released under the MIT License.
