# cartoon_api_node

Fetch 2D or 3D Cartoon Datasets via Public APIs

## Features
- Dynamically fetches 2D or 3D cartoon data from public APIs
- Selects the appropriate dataset based on parameter input (`cartoon_type`)
- Outputs serialized cartoon data or descriptive error messages

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
  - id: cartoon_api_node
    build: pip install -e .
    path: cartoon_api_node
    inputs:
      cartoon_type: input/cartoon_type
    outputs:
      - cartoon_data
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
  - id: type_source
    build: pip install your-node
    path: your-type-source-node
    outputs:
      - cartoon_type

  - id: cartoon_api_node
    build: pip install -e .
    path: cartoon_api_node
    inputs:
      cartoon_type: type_source/cartoon_type
    outputs:
      - cartoon_data
```

Your point source must output:

* Topic: `cartoon_type`
* Data: string ("2d" or "3d")
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Specifies cartoon type: '2d' or '3d'"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                |
| -------------| ------ | ------------------------------------------ |
| cartoon_type  | string | Specifies cartoon type: '2d' or '3d'       |

### Output Topics

| Topic         | Type   | Description                                          |
| -------------| ------ | ---------------------------------------------------- |
| cartoon_data  | dict   | List of cartoon info objects or error dict (as JSON) |


## License

Released under the MIT License.
