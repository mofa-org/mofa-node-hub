# color_api_node

Color API Node: Dora node for aggregating color analysis from two REST API endpoints at serialif.com.

## Features
- Queries multiple color analysis endpoints and aggregates results
- Robust error handling for each API endpoint
- Outputs unified color data in JSON format

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
  - id: color_api_node
    build: pip install -e .
    path: color_api_node
    outputs:
      - color_data
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
  - id: your_input_node
    outputs:
      - user_input
  - id: color_api_node
    build: pip install -e .
    path: color_api_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - color_data
```

Your point source must output:

* Topic: `user_input`
* Data: (can be empty or any standard input, not used by this node)
* Metadata:

  ```json
  {
      "dtype": "string",
      "description": "(Optional) Input string for framework compatibility. Not used."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                 |
| ---------- | ------ | -------------------------- |
| user_input | string | (Optional) Input parameter. Ignored by node, for flow compatibility. |

### Output Topics

| Topic      | Type   | Description                                         |
| ---------- | ------ | --------------------------------------------------- |
| color_data | dict   | Aggregated JSON responses or errors from color API endpoints. |


## License

Released under the MIT License.

````
