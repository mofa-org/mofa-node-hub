# dummyapi_client_node

A Dora-rs node for querying the DummyAPI products endpoint and publishing the response via Dora messaging. Easily integrates external REST data sources into your Dora/MoFA pipelines.

## Features
- Fetches product data from https://dummyapi.online/api/products
- Standardizes error and data output to downstream nodes
- Simple integration for any Dora/MoFA pipeline

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
  - id: dummyapi_client
    build: pip install -e dummyapi_client_node
    path: dummyapi_client_node
    inputs:
      user_input: input/user_input
    outputs:
      - dummyapi_products
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
    build: pip install your-point-source-node
    path: your-point-source-node
    outputs:
      - user_input

  - id: dummyapi_client
    build: pip install -e dummyapi_client_node
    path: dummyapi_client_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - dummyapi_products
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (can be ignored by this node, but required for agent triggering)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Any string; not used but required to trigger dummyapi fetch."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                     |
| ----------| ------ | ----------------------------------------------- |
| user_input | string | Triggers a fetch from DummyAPI; content ignored |

### Output Topics

| Topic             | Type          | Description                                           |
| ---------------- | ------------- | ----------------------------------------------------- |
| dummyapi_products | dict or error | Products from DummyAPI, or error message if fetch fails|

## License

Released under the MIT License.
