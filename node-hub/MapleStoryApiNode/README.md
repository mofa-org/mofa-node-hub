# maplestory_api_node

A Dora-rs node for querying available MapleStory game data versions using the `maplestory.io` API. It wraps the HTTP API endpoint into a node interface, makes results accessible to other nodes, and returns any retrieval errors in a standardized format.

## Features
- Fetches supported MapleStory versions from maplestory.io
- Exposes game version data for downstream Dora nodes
- Handles API errors gracefully and returns error information

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
  - id: maplestory_versions_node
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input
    outputs:
      - maplestory_versions
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
  - id: source_node
    build: pip install your-node
    path: your-source-node
    outputs:
      - user_input
  - id: maplestory_versions_node
    build: pip install -e .
    path: .
    inputs:
      user_input: source_node/user_input
    outputs:
      - maplestory_versions
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or object (as required)
* Metadata:

  ```json
  {
    "type": "string",
    "purpose": "To provide an optional trigger or query parameter for the MapleStory API node."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                    |
|-------------|--------|------------------------------------------------|
| user_input  | string | Optional parameter; triggers the API request.  |

### Output Topics

| Topic                | Type     | Description                                   |
|----------------------|----------|-----------------------------------------------|
| maplestory_versions  | object   | JSON response from maplestory.io or error info |

## License

Released under the MIT License.
