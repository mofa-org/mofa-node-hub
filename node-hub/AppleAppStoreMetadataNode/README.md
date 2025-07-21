# apple_appstore_node

Fetch Apple App Store metadata for a specific app using an external API.

## Features
- Retrieves metadata for Apple App Store apps via HTTP API
- Handles errors with JSON error output
- Plugin-ready as a MofaAgent Dora node

## Getting Started

### Installation
Install via cargo:
```bash

pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: appstore_metadata
    build: pip install -e apple_appstore_node
    path: apple_appstore_node
    inputs:
      user_input: input/user_input  # Optional, placeholder input
    outputs:
      - appstore_metadata
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
    path: my-input-node
    outputs:
      - user_input

  - id: appstore_metadata
    build: pip install -e apple_appstore_node
    path: apple_appstore_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - appstore_metadata
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (not used, serves as trigger)
* Metadata:

  ```json
  {"format": "any", "description": "Trigger input, not used in processing"}
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                        |
| ---------- | ------- | ---------------------------------- |
| user_input | Any     | Placeholder/trigger input (unused) |

### Output Topics

| Topic             | Type   | Description                                        |
| ----------------- | ------ | -------------------------------------------------- |
| appstore_metadata | object | JSON metadata for app, or error message in {'error': str} |


## License

Released under the MIT License.

````