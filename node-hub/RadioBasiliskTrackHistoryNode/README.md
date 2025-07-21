# radio_basilisk_node

A Dora-rs node to fetch Radio Basilisk channel track history via API. This node makes HTTP requests and emits responses through the Dora framework for integration with other nodes.

## Features
- Retrieve recent track history from Radio Basilisk
- Expose JSON or error response to downstream nodes
- Plug-and-play integration via Dora messaging system

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
  - id: track_history_node
    build: pip install -e .
    path: radio_basilisk_node
    inputs:
      user_input: dora/input/user_input
    outputs:
      - track_history
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
    build: pip install your-node
    path: your-point-source-node
    outputs:
      - user_input

  - id: track_history_node
    build: pip install -e .
    path: radio_basilisk_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - track_history
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (serves as a trigger for fetching)
* Metadata:

  ```json
  {
    "description": "Any value/trivial, used to trigger the HTTP request for track history."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                           |
| ----------- | -------- | ------------------------------------- |
| user_input  | any      | Used as a trigger to fetch track data |

### Output Topics

| Topic         | Type   | Description                                             |
| ------------- | ------ | ------------------------------------------------------- |
| track_history | object | Track history data from Radio Basilisk API, or error   |


## License

Released under the MIT License.
