# healthcare_content_node

Retrieve Healthcare.gov Content via Dora Node

## Features
- Fetches up-to-date content from Healthcare.gov public API
- Returns structured JSON suitable for downstream processing
- Simple integration into Dora or MOFA agent pipelines

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
  - id: healthcare_content
    build: pip install -e .
    path: healthcare_content_node
    inputs:
      user_input: input/user_input
    outputs:
      - api_response
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
  - id: user_input
    build: pip install your-custom-node
    path: your_custom_node
    outputs:
      - user_input

  - id: healthcare_content
    build: pip install -e .
    path: healthcare_content_node
    inputs:
      user_input: user_input/user_input
    outputs:
      - api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (input forwarding for chaining)
* Metadata:

  ```json
  {
    "data_type": "string",
    "description": "Arbitrary string to facilitate chaining; not directly used"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                           |
| ----------| ------ | ----------------------------------------------------- |
| user_input | string | Arbitrary input (for chaining; not used by this node) |

### Output Topics

| Topic        | Type      | Description                       |
| ------------|-----------|-----------------------------------|
| api_response | JSON dict | JSON from Healthcare.gov API or error string |

## License

Released under the MIT License.
