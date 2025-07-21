# traffic_metadata_node

A Dora-rs node for retrieving and streaming live traffic dataset metadata from the ACT government's open data API. This node acts as a data ingestion component, supporting integration with point or image processing nodes in a Dora dataflow pipeline.

## Features
- Fetches real-time traffic metadata from ACT Government open data API
- Sends structured JSON output downstream for pipeline consumption
- Configurable through Dora parameters

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
  - id: traffic_metadata_node
    build: pip install -e traffic_metadata_node
    path: traffic_metadata_node
    inputs:
      user_input: input/user_input
    outputs:
      - traffic_metadata
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
    build: pip install your-point-source
    path: your-point-source
    outputs:
      - user_input

  - id: traffic_metadata_node
    build: pip install -e traffic_metadata_node
    path: traffic_metadata_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - traffic_metadata
```

Your point source must output:

* Topic: `user_input`
* Data: any serializable value, used as trigger for API retrieval
* Metadata:

  ```json
  {
    "description": "String or JSON-serializable object, used to trigger traffic metadata retrieval."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type         | Description                        |
| ----------- | ------------ | ---------------------------------- |
| user_input  | any/json     | Triggers fetching traffic metadata |

### Output Topics

| Topic           | Type        | Description                                                      |
| --------------- | ----------- | ---------------------------------------------------------------- |
| traffic_metadata | json       | Traffic metadata from the ACT open data API or error information |

## License

Released under the MIT License.
