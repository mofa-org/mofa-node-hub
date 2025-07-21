# realip_node

A Dora-rs node to fetch and expose external IP information using the public realip.cc API. Compatible with MofaAgent, this node enables seamless integration into Dora pipelines and agent networks for automated or programmatic retrieval of IP metadata.

## Features
- Fetches external (public) IP address and info from realip.cc.
- Simple, stateless API call with minimal input (useful for chainable pipelines).
- Graceful error handling with informative responses.

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
  - id: realip_node
    build: pip install -e realip_node
    path: realip_node
    inputs:
      user_input: input/user_input  # Symbolic; contents ignored
    outputs:
      - ip_info
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
  - id: my_node
    build: pip install my-node
    path: my-node
    outputs:
      - user_input

  - id: realip_node
    build: pip install -e realip_node
    path: realip_node
    inputs:
      user_input: my_node/user_input
    outputs:
      - ip_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable payload (the contents are ignored by this node, but the parameter is required for compatibility)
* Metadata:

  ```json
  {
    "input": "required, any type or payload (ignored by realip_node)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type           | Description                              |
| ---------- | -------------- | ---------------------------------------- |
| user_input | Any / Ignored  | Required for pipeline chaining; ignored. |

### Output Topics

| Topic   | Type                     | Description                                                        |
| ------- | ------------------------ | ------------------------------------------------------------------ |
| ip_info | Dict, String, or Err Dict| JSON API response from realip.cc, or error message information     |

## License

Released under the MIT License.
