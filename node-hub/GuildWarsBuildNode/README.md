# guild_wars_build

Fetch Guild Wars 2 Live Build Information via Dora-rs Node

## Features
- Fetches current Guild Wars 2 build info from public API
- Simple Dora integration with universal input compatibility
- Robust error handling for API failures

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
  - id: build_fetcher
    path: guild_wars_build
    build: pip install -e guild_wars_build
    inputs:
      user_input: input/user_input
    outputs:
      - build_info
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
  - id: data_source
    path: your_data_source
    build: pip install -e your_data_source
    outputs:
      - user_input

  - id: build_fetcher
    path: guild_wars_build
    build: pip install -e guild_wars_build
    inputs:
      user_input: data_source/user_input
    outputs:
      - build_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any (ignored, but must be present for message/call chain)
* Metadata:

  ```json
  {
    "type": "any",
    "usage": "Compatibility trigger for node; data content is ignored"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                 |
| ---------- | ------ | ------------------------------------------- |
| user_input | any    | Compatibility parameter, ignored by node.   |

### Output Topics

| Topic      | Type | Description                                    |
| ---------- | ---- | ---------------------------------------------- |
| build_info | dict | API response from Guild Wars 2 build endpoint. |

## License

Released under the MIT License.
