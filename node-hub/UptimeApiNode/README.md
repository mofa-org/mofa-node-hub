# uptime_api_node

A Dora-rs node that fetches the current uptime status from the [uptime.is](https://uptime.is) public API and exposes it as a message output in your Dora pipeline.

## Features
- Simple integration to retrieve uptime status via REST API
- Robust error handling for network and serialization faults
- Compatible with inter-node dataflow (accepts upstream user input for chaining)

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
  - id: uptime_api_node
    build: pip install -e .
    path: uptime_api_node
    inputs:
      user_input: your_source/user_input
    outputs:
      - uptime_api_result
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
  - id: your_source
    build: pip install your-source-package
    path: your-source-path
    outputs:
      - user_input

  - id: uptime_api_node
    build: pip install -e .
    path: uptime_api_node
    inputs:
      user_input: your_source/user_input
    outputs:
      - uptime_api_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any upstream message for API chaining (can be dummy input for stateless use)
* Metadata:

  ```json
  {
    "description": "Arbitrary trigger or input payload for uptime_api_node",
    "required": false
  }
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                      |
|------------|-----------|----------------------------------|
| user_input | any/json  | Input message to trigger API call |

### Output Topics

| Topic             | Type         | Description                                |
|-------------------|--------------|--------------------------------------------|
| uptime_api_result | json/string  | Uptime API result or error message payload |

## License

Released under the MIT License.
