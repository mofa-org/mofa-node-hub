# carbon_intensity_node

A Dora-rs node that queries and retrieves UK National Grid Carbon Intensity API data, including current, daily, and historical carbon intensity, as well as emission factors for fuel types. Outputs all data in a single unified message for downstream pipeline consumption.

## Features
- Fetches carbon intensity emission factors per fuel type
- Retrieves current, daily, and specific-date carbon intensity data
- Aggregates all query results into a single output for easy integration

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
  - id: carbon_intensity
    build: pip install -e .
    path: carbon_intensity_node
    inputs:
      user_input: input/user_input
    outputs:
      - carbon_intensity_data
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
  - id: your_input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input

  - id: carbon_intensity
    build: pip install -e .
    path: carbon_intensity_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - carbon_intensity_data

  - id: your_consumer
    build: pip install your-consumer-node
    path: your-consumer-node
    inputs:
      carbon_intensity_data: carbon_intensity/carbon_intensity_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (required for Dora pipeline startup, ignored by this node)
* Metadata:

  ```json
  {
    "type": "string or any",
    "description": "Dummy input required to maintain dataflow compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ---------- | ------ | ----------------------------------------- |
| user_input | Any    | Dummy input to activate dataflow; ignored. |

### Output Topics

| Topic                 | Type   | Description                                                       |
| --------------------- | ------ | ----------------------------------------------------------------- |
| carbon_intensity_data | Dict   | Dictionary with all queried UK Carbon Intensity API payloads.      |

## License

Released under the MIT License.
