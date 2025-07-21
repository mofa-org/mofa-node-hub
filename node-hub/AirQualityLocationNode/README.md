# air_quality_node

AirQualityLocationNode: A Dora-rs/MoFA agent node that retrieves real-time air quality location data from OpenAQ. It fetches information about a specific monitoring location as well as a list of all available locations, providing structured results or error messages for downstream pipeline processing.

## Features
- Fetches specific air quality monitoring location metadata from OpenAQ
- Retrieves up-to-date listings of all available air quality monitoring locations
- Robust error handling with informative output messages

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
  - id: air_quality_node
    build: pip install -e .
    path: air_quality_node
    outputs:
      - air_quality_outputs
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
  - id: my_input_node
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - user_input

  - id: air_quality_node
    build: pip install -e .
    path: air_quality_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - air_quality_outputs
```

Your point source must output:

* Topic: `user_input`
* Data: Any placeholder data (not used by this node, but required for pipeline compatibility)
* Metadata:

  ```json
  {
    "desc": "Placeholder input for compatibility. Content is ignored by air_quality_node."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                |
| ----------- | ------ | ------------------------------------------ |
| user_input  | any    | Placeholder input for compatibility        |

### Output Topics

| Topic               | Type                | Description                                                 |
| ------------------- | ------------------- | ----------------------------------------------------------- |
| air_quality_outputs | dict                | Dict with 'letzigrund_info' and 'all_locations', or errors |


## License

Released under the MIT License.
