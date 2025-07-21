# nationalize_api_node

Predicts the nationality of a given name using the [nationalize.io](https://nationalize.io) API.

## Features
- Predict nationality probabilities for any given first name
- Simple REST API call integration (nationalize.io)
- Robust input validation and error handling

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
  - id: nationalize_api_node
    build: pip install -e .
    path: nationalize_api_node
    inputs:
      name: input/name
    outputs:
      - nationalize_result
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
  - id: your_node
    build: pip install your-node
    path: your-node
    outputs:
      - name
  - id: nationalize_api_node
    build: pip install -e .
    path: nationalize_api_node
    inputs:
      name: your_node/name
    outputs:
      - nationalize_result
```

Your point source must output:

* Topic: `name`
* Data: String (name to be predicted)
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "Name to predict nationality for"
  }
  ```

## API Reference

### Input Topics

| Topic  | Type   | Description                             |
|--------|--------|-----------------------------------------|
| name   | string | Name whose nationality is to be inferred |

### Output Topics

| Topic              | Type  | Description                              |
|--------------------|-------|------------------------------------------|
| nationalize_result | dict  | Nationalize.io API result or error report |


## License

Released under the MIT License.
