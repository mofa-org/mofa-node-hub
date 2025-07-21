# food_hygiene_node

Fetch and relay UK Food Hygiene Rating data as a Dora node.

## Features
- On-demand retrieval of comprehensive UK Food Hygiene Rating dataset from Food Standards Agency
- Provides upstream dataflow compatibility with configurable user inputs
- Robust error handling with serializable result output

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
  - id: food_hygiene
    build: pip install -e food_hygiene_node
    path: food_hygiene_node
    inputs:
      user_input: input/user_input
    outputs:
      - food_hygiene_data
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
  - id: user_source
    build: pip install your-user-source
    path: your-user-source
    outputs:
      - user_input

  - id: food_hygiene
    build: pip install -e food_hygiene_node
    path: food_hygiene_node
    inputs:
      user_input: user_source/user_input
    outputs:
      - food_hygiene_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable user input
* Metadata:

  ```json
  {
    "type": "string",
    "purpose": "Pass-through or future filtering of food hygiene queries"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                 |
| ----------| ------ | --------------------------------------------|
| user_input | Any    | Dummy input for pipeline flow; can be used for query parameters or triggering fetch |

### Output Topics

| Topic              | Type   | Description                                   |
| ------------------ | ------ | ---------------------------------------------- |
| food_hygiene_data  | dict   | Complete response from Food Hygiene Ratings API, or error report |


## License

Released under the MIT License.
