# bangladesh_nid_node

A Dora-rs node for interacting with the Bangladesh NID Application System API. Allows retrieval of general endpoint data via an HTTP GET request for downstream use in a Dora pipeline.

## Features
- Queries the Bangladesh NID API via HTTP GET
- Yoga-friendly: works in Dora data graphs as a plug-and-play source
- Handles and returns errors in agent output

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
  - id: bangladesh_nid_api
    build: pip install -e bangladesh_nid_node
    path: bangladesh_nid_node
    inputs:
      user_input: input/user_input
    outputs:
      - bangladesh_nid_api_response
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
  - id: my_other_node
    build: pip install my-other-node
    path: my-other-node
    outputs:
      - user_input
  - id: bangladesh_nid_api
    build: pip install -e bangladesh_nid_node
    path: bangladesh_nid_node
    inputs:
      user_input: my_other_node/user_input
    outputs:
      - bangladesh_nid_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or object (placeholder – not used by the node but required for wiring in Dora)
* Metadata:

  ```json
  {
    "description": "Placeholder input for triggering NID API node",
    "required": false,
    "type": "string or object"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                              |
| ---------- | ------ | ---------------------------------------- |
| user_input | any    | Placeholder input for datagraph trigger   |

### Output Topics

| Topic                        | Type                | Description                        |
| ---------------------------- | ------------------- | ---------------------------------- |
| bangladesh_nid_api_response  | dict or str or list | The response from the NID API call |

## License

Released under the MIT License.
