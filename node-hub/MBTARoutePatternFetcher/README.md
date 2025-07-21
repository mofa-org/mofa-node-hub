# mbta_route_pattern

Fetch MBTA Route Patterns as a Dora-rs Node.

## Features
- Retrieves MBTA Commuter Rail Providence line route patterns from MBTA V3 API
- Facilitates communication via Dora-rs API with exposure of input/output topics
- Handles HTTP errors and JSON serialization, returning robust error objects

## Getting Started

### Installation
Install via cargo:
```bash

pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: mbta_pattern_fetcher
    build: pip install -e .
    path: mbta_route_pattern
    inputs:
      user_input: input/user_input
    outputs:
      - route_patterns
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
  - id: your_downstream_node
    build: pip install your-node         # Replace with your node's install step
    path: your-downstream-node           # Replace with your node's path
    inputs:
      route_patterns: mbta_pattern_fetcher/route_patterns
```

Your point source must output:

* Topic: `points_to_track`
* Data: Flattened array of coordinates
* Metadata:

  ```json
  {
    "num_points": N,
    "dtype": "float32",
    "shape": [N, 2]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                             |
|-----------|---------|-----------------------------------------|
| user_input | object  | Triggers a fetch (can be null or empty) |

### Output Topics

| Topic          | Type   | Description                                              |
|---------------|--------|---------------------------------------------------------|
| route_patterns| object | MBTA route patterns result, or error information object  |


## License

Released under the MIT License.
