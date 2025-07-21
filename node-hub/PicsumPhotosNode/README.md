# picsum_photos_node

A Dora-rs node for fetching random photo metadata from the picsum.photos public API. Returns a list of random photo objects upon request for downstream processing in a Dora pipeline.

## Features
- Fetches random stock photo metadata from picsum.photos
- Robust error handling with user-friendly error messages
- Simple input/output integration for use in multi-node pipelines

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
  - id: picsum_node
    build: pip install -e picsum_photos_node
    path: picsum_photos_node
    inputs:
      user_input: input/user_input
    outputs:
      - picsum_photos_list
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
    build: pip install your-node  # Replace with your node's build instructions
    path: your-point-source-node  # Replace with your node's path
    outputs:
      - user_input    # Output expected for this node to start processing

  - id: picsum_node
    build: pip install -e picsum_photos_node
    path: picsum_photos_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - picsum_photos_list
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable user command or an empty payload
* Metadata:

  ```json
  {
    "type": "string or null",
    "desc": "Optional staged input parameter; not required."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description              |
|-------------|---------|--------------------------|
| user_input  | string  | Dummy input to trigger photos fetch |

### Output Topics

| Topic              | Type   | Description                    |
|--------------------|--------|--------------------------------|
| picsum_photos_list | object | List of photo metadata or error info |


## License

Released under the MIT License.
