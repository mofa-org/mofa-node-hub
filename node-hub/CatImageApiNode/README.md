# cat_image_node

A Dora-rs node for fetching random cat images in JSON format from the CATAAS public API. This node demonstrates integration with remote HTTP endpoints and simple input/output parameter handling.

## Features
- Fetches random cat image metadata from cataas.com API
- Forwards JSON responses (including error information) to the output topic
- Seamless integration with Dora-rs pipelines and custom user message inputs

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
  - id: cat_image
    build: pip install -e ./cat_image_node
    path: cat_image_node
    inputs:
      user_input: input/user_input
    outputs:
      - cat_image_json
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
  - id: image_requester
    build: pip install your-custom-node
    path: your_image_requester
    outputs:
      - user_input

  - id: cat_image
    build: pip install -e ./cat_image_node
    path: cat_image_node
    inputs:
      user_input: image_requester/user_input
    outputs:
      - cat_image_json
```

Your point source must output:

* Topic: `user_input`
* Data: Any type (optional, used to trigger the API call)
* Metadata:

  ```json
  {
    "description": "Optional trigger parameter, pass-through or custom data. Ignored by node but required for connection."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type     | Description                                  |
| ---------- | -------- | -------------------------------------------- |
| user_input | Any      | Optional trigger or configuration parameter. |

### Output Topics

| Topic           | Type   | Description                          |
| --------------- | ------ | ------------------------------------ |
| cat_image_json  | dict   | Cat image metadata or error message.  |

## License

Released under the MIT License.
