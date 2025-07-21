# poetry_dowson_node

Fetch poems by Ernest Dowson from PoetryDB as a Dora node

## Features
- Query all poems by Ernest Dowson from PoetryDB
- Retrieve poems containing the word "love" in the title
- Outputs both raw results and error details for robust workflow handling

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
  - id: poetry_dowson
    build: pip install -e poetry_dowson_node
    path: poetry_dowson_node.py
    inputs:
      user_input: input/user_input
    outputs:
      - poetrydb_results
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
    build: pip install your-input-node
    path: your-input-node.py
    outputs:
      - user_input

  - id: poetry_dowson
    build: pip install -e poetry_dowson_node
    path: poetry_dowson_node.py
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - poetrydb_results
```

Your point source must output:

* Topic: `user_input`
* Data: Free-form string or dict representing user input (not directly used here, but needed for compatibility)
* Metadata:

  ```json
  {
    "description": "User input for poetry queries (optional, not used)",
    "type": "string or dict"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type           | Description                       |
| ----------- | -------------- | --------------------------------- |
| user_input  | Any (string/dict) | Optional user query/placeholder    |

### Output Topics

| Topic             | Type       | Description                                                  |
| ----------------- | ---------- | ------------------------------------------------------------ |
| poetrydb_results  | dict       | PoetryDB results or error details (see below for keys)       |


## License

Released under the MIT License.
